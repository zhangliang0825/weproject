import asyncio
import csv
import json
import logging
import re
import time

import async_timeout
import pymysql
from loguru import logger
from aiomysql import OperationalError
from retrying import retry
import aiohttp
from lxml import etree
import aiomysql

CONCURRENCY = 30
semaphore = asyncio.Semaphore(CONCURRENCY)
stop = False
all_data_urls = set()
urls = []
links_detail = set()  #爬取中的详情页链接的集合
crawled_links_detail = set()

g_pool = None

#建立一个请求的异步
headers = {

  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


file = csv.reader(open('基金公司名单.csv','r',encoding='utf-8'))
all_jj_name_ = {j :i[0] for i in file for j in i[1].split("|")}

async def post(session,url):


    headers = {

  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',

}

    async with semaphore:
        with async_timeout.timeout(8):
            await asyncio.sleep(0.1)

            async with session.get(url, headers=headers,) as response:

                if response.status == 200:
                    # print(await response.text(encoding='utf-8'))
                    return await response.text(encoding='utf-8')


@retry(stop_max_attempt_number=10)
async def fetch(session,url,):
            async with semaphore:
                try:
                    with async_timeout.timeout(8):
                            await asyncio.sleep(0.1)
                            async with session.get(url,headers=headers) as response:
                                print(222222,response.status)
                                if response.status == 200:

                                    return await response.text(encoding='utf-8')
                except Exception as e:
                    print(e)

# async def update_data(sql):
#     global g_pool
#     with (await g_pool) as conn:
#         cursor = await conn.cursor()
#
#         await cursor.execute(sql)
#         print(cursor.rowcount)



async def run(sql,key,values):

    conn = await aiomysql.connect(host='120.26.211.213', user='julai01', password='Zycj@2020688', db='wemedia', charset='utf8mb4',)
    # conn = await aiomysql.connect(host='120.26.106.222', user='julai01', password='Sh51785136@sh', db='jijin',
    #     charset='utf8mb4', )

    cursor = await conn.cursor()
    await cursor.execute(sql,(key,values))
    num = cursor.rowcount

    await conn.commit()
    conn.close()


async def parse(html):
    HTML = etree.HTML(html)
    all_data_list = HTML.xpath("//div[@class='common-left-menu ttjj-grid-4']/ul/li/div[@class='sub-link']/a")
    for info in all_data_list:
        link = 'http://fund.eastmoney.com'+info.xpath("./@href")[0]
        name = info.xpath("./text()")[0]
        all_data_urls.add( (link,name))
    return  all_data_urls

def is_char(text,jj_name):
    text_s = text.replace(jj_name, '')
    reslut_char = [i for i, j in enumerate(list(text_s)) if '\u4e00' <= j <= '\u9fff']
    if all(i in reslut_char for i in [0,1]):
        reslut_text =  jj_name + text_s[:2]
    elif not all(i in reslut_char for i in [0,1]):
        if len(reslut_char)==2:
            reslut_text = jj_name + text_s[:reslut_char[1]+1]
        if len(reslut_char) > 2:
            reslut_text =  jj_name + text_s[:reslut_char[1]+1]
        if len(reslut_char)==1:
            reslut_text =  jj_name + text_s
    return reslut_text

def detail_detail_gaoguan(html,name):
    g_json_data = json.loads(html)
    gaoguan_name = [' {} [[GG]]={}/'.format(name,i.get('NAME')) for i in  g_json_data.get('Data') if any(j in i.get('POST') for j in ['董事长','总经理','副总经理','总裁','副总裁','副董事长'])]
    return gaoguan_name

def detail_jjll(html,name):
    HTML = etree.HTML(html)
    all_datas = HTML.xpath("//div[@class='table-content']/p/a/text()")
    all_datas = [' {} [[JL]]={}/'.format(name, i.strip()) for i in all_datas]
    return all_datas


async def parse_details(html,name,session,url):
    all_data_dict = {}
    code = re.search(r'\d+', url).group(0)
    HTML = etree.HTML(html)
    all_data_ = HTML.xpath("//div[@class='jcommon-block-con common-block-con']//tbody/tr|//div[@class='third-block']//tbody/tr")
    name = name.split("基金")[0]
    # if name in ['上海海通证券资产管理','广发资产管理','国泰君安资产管理']:
    #     pass
    all_jj_name_1 = {
        '国泰君安资产管理':'国君资管',
        '上海海通证券资产管理':'海通资管',
        '广发资产管理':'广发资管'
    }
    all_jj_name_.update(all_jj_name_1)
    if name in all_jj_name_:
        name = all_jj_name_.get(name)
    else:
        name = name
    #{} [[GS]]=={}基金/
    all_cp_data = ['{} [[GS]]=={}基金/'.format(name,name),]
    for info in all_data_:
        jj_name = info.xpath("./td[@class='fund-name-code']/a[1]/text()")
        if jj_name ==[]:
            continue
        jj_name = jj_name[0]
        if name in jj_name:

            result_tags = is_char(jj_name,name)
        else:
            result_tags = jj_name[:len(name)+2]
        jj_name_re = ' {} [[CP]]={}/'.format(name,result_tags)
        all_cp_data.append(jj_name_re)

    detail_url = f'http://fund.eastmoney.com/Company/jbzl/GetManager?gsId={code}&pageIndex=0&pageSize=100&type=1'
    detail_html = await fetch(session,detail_url)
    gaoguan_result = detail_detail_gaoguan(detail_html,name)

    jl_url = f'http://fund.eastmoney.com/Company/f10/jjjl_{code}.html'

    detail_jl_html = await fetch(session,jl_url)
    jjll_result = detail_jjll(detail_jl_html,name)
    all_data_cjg = all_cp_data+gaoguan_result+jjll_result
    all_data_cjg__ = sorted(list(set(all_data_cjg)),key= all_data_cjg.index)
    all_data_dict.setdefault(name,[]).append(''.join(all_data_cjg__))
    for key,values in all_data_dict.items():

        key = 'tongyici{}'.format(key)
        print(key, values)
        sql = 'update sysparam set info =%s where variable = %s'
        # sql = 'insert into sysparam ( info,variable) values (%s,%s)'
        await run(sql,values,key)


#建立一个请求session
async def download(url,):
     async with aiohttp.ClientSession() as session:
         html = await fetch(session,url)
         return await parse(html)


async def download2(url,name):

    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        if html:
            await parse_details(html,name,session,url)
        else:
            await download2(url,name)
            # crawled_links_detail.add(url)
            # print(url)


async def run2():
    # asyncio.sleep(1)
    # conn = await aiomysql.connect(host='120.26.211.213', user='julai01', password='Zycj@2020688', db='wemedia',
    #     charset='utf8mb4', )
    # cursor = await conn.cursor()
    # await conn.ping(reconnect=True)
    # sql = 'SELECT variable,info FROM sysparam WHERE variable LIKE "%tongyici%"'
    #
    # await cursor.execute(sql)
    await asyncio.sleep(1)
    # dict_reslut = {key.strip('tongyici'): value.strip() for key, value in await cursor.fetchall()}
    with open('tongyici.txt', 'r') as f:
        dict_reslut = eval(f.read())


    # await cursor.close()
    # conn.close()
        return dict_reslut

    # await conn.commit()
    #


async  def haomai_parse_(html):
    asyncio.sleep(1)

    dict_reslut = await run2()

    # for variable,info in reslut_s:
    HTML = etree.HTML(html)
    # data_list = HTML.xpath("//div[@id = 'nTab30_1']//table//tr[position()>1]/td[2]//text()")


    name = HTML.xpath("//div[@class='fund_name ftYahei fl']/text()")[0].split('基金')[0]

    zaizhi_name_list = HTML.xpath("//div[@id = 'nTab30_0']//table//tr[position()>1]/td[2]//text()")
    lizhi_name_list = HTML.xpath("//div[@id = 'nTab30_1']//table//tr[position()>1]/td[2]//text()")
    diff_name = set(lizhi_name_list) - set(zaizhi_name_list)
    data_list = list(diff_name)

    print(data_list,222222221)
    if name in all_jj_name_:
        name = all_jj_name_[name]
    else:
        name = name

    data_list = dict_reslut.get(name,'')+''.join([' {} [[LZ]]={}/'.format(name,i) for i in data_list])

    sql = 'update sysparam set info =%s where variable = %s'

    await run(sql, data_list,'tongyici'+name)


async def download_haomai(url,):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session,url)
        if html:
            await haomai_parse_(html)
        else:
            await download_haomai(url,)

all_haomai_data = []


async def haomai_detail_parse(session,html):
    json_html = json.loads(html)
    for info in json_html.get('list'):
        jj_code = info.get('jgdm')
        jj_name = info.get('jgjc')
        index_url = 'https://www.howbuy.com/fund/company/{}/managerlist'.format(jj_code)

        all_haomai_data.append(index_url)
    return all_haomai_data



async def haomai(url):
    async with aiohttp.ClientSession() as session:
        html = await post(session, url)
        return await haomai_detail_parse (session,html)


if __name__ == '__main__':
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # get_future = asyncio.ensure_future(download("http://fund.eastmoney.com/Company/80538609.html"))
    # loop.run_until_complete(get_future)
    # result_URL = get_future.result()
    # result = [i for i in result_URL]
    #
    # tasks = [asyncio.ensure_future(download2(i[0],i[1])) for i in result]
    #
    # asyreslut = asyncio.gather(*tasks)
    # loop.run_until_complete(asyreslut)
    # end_time = time.time()
    # print(end_time - start_time)


    loop = asyncio.get_event_loop()
    get_future = asyncio.ensure_future(haomai('https://www.howbuy.com/fund/company/ajax.htm'))
    loop.run_until_complete(get_future)
    result_URL = get_future.result()
    result = [i for i in result_URL ]

    tasks = [asyncio.ensure_future(download_haomai(i)) for i in result ]
    asyreslut = asyncio.gather(*tasks)
    loop.run_until_complete(asyreslut)



