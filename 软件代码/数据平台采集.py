import csv
import itertools
import logging
from  datetime import datetime
import json

import re
import time

import aiomysql

import aiohttp
import asyncio

nows = datetime.now()
current_month = datetime.strftime(datetime(nows.year, nows.month, 1),'%Y-%m-%d 00:00:00')

now = datetime.now()
currentday = datetime.strftime(datetime(now.year, now.month, now.day), '%Y%m%d')

# last_month_start = datetime.strftime(datetime(now.year, now.month-1, 1), '%Y%m%d')
# last_month_middle =datetime.strftime(datetime(now.year, now.month-1, 15), '%Y%m%d')
# last_month_end = datetime.strftime(datetime(now.year, now.month-1, 31), '%Y%m%d')

headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

# 'Cookie':'passport_csrf_token_default=ab3715eef42f24ce85eba051279b4a8f; ttwid=1%7CEQqaQRGYqJHbM6vjddSmseATuLjWIh4Z9_nFPJ-svOk%7C1622256706%7C1f696e3b542d66b8a943a7f0cb6b99906dfe8c26d74a81bdfbbf23c0eb43c2a5; WIN_WH=352_546; PIXIEL_RATIO=1.5; FRM=new; tt_webid=6951613006950188581; s_v_web_id=verify_cbff3704ff2a8f82867b9ac9bb74260f; _S_WIN_WH=1280_562; _S_DPR=1.5; _S_IPAD=0; MONITOR_WEB_ID=6951613006950188581',

'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
}





'''
mysql 异步版本
'''

logobj = logging.getLogger('mysql')


class Pmysql:
    __connection = None

    def __init__(self):
        self.cursor = None
        self.connection = None

    @staticmethod
    async def getconnection():
        if Pmysql.__connection == None:
            conn = await aiomysql.connect(
                host='120.26.106.222',
                port=3306,
                user='julai01',
                password='Sh51785136@sh',
                db='jijin',
            )
            if conn:
                Pmysql.__connection = conn

                return conn
            else:
                raise ("connect to mysql error ")
        else:
            print(Pmysql.__connection, 111111111111)
            return Pmysql.__connection

    async def query(self, query, args=None):

        self.cursor = await self.connection.cursor()
        # 每次进行查询操作时都先执行一下ping()方法来检查一下连接是否有效
        await self.connection.ping()
        await self.cursor.execute(query, args)
        r = await self.cursor.fetchall()
        await self.cursor.close()
        return r

    async def execute(self, query, conn, args=None):
        self.cursor = await self.connection.cursor()
        await self.connection.ping()
        await self.cursor.execute(query, args)
        await conn.commit()
        if self.cursor.rowcount == 0:
            return False
        else:
            return True

from retrying import retry
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

now = datetime.now()
current_month = datetime.strftime(datetime(now.year, now.month, now.day), '%Y%m%d')


async def fetch(url, semaphore):
    async with semaphore:
        await asyncio.sleep(0.6)
        while True:
            try:

                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers, timeout=8) as response:
                        reslut_text = await response.text(encoding='utf-8')
                        return reslut_text
            except:
                print(url,'请求超时..,再次发送请求..')


crawled_num_mayi_data = 0

@retry(stop_max_attempt_number =10)
async def detail_data_mayi(title, link, media, str_date, semaphore):
    global crawled_num_mayi_data
    url = f'https://mobilegw.alipay.com/mgw.htm?operationType=alipay.secuprod.secuc' \
        f'ommunity.comment.getH5Comment&requestData=%5B%7B%22commentId%22%3A%22{link}%22%7D%5D&_=1622599907073&callback=1'
    comment_url = f'https://think.klv5qu.com/p/f/fd-j1xcs5me/comment-share.html?commentId={link}&hasSpace=NO'
    html_text = await fetch(url, semaphore)
    if '访问已经删除的言论' not in html_text:

        # if '号' in media:
        #     json_data = json.loads(html_text[2:-1]).get("result").get("comment")
        # else:
        json_data = json.loads(html_text[2:-1]).get("result").get("comment")
        readCount = json_data.get("readCount", 0)
        popCount = json_data.get("popCount", 0)
        replyCount = json_data.get("replyCount", 0)
        attitude1 = [i.get('count', 0) for i in json_data.get("attitude") if i.get("id") == 'jiayou'][0]
        attitude2 = [i.get('count', 0) for i in json_data.get("attitude") if i.get("id") == 'xiaochusheng'][0]
        attitude3 = [i.get('count', 0) for i in json_data.get("attitude") if i.get("id") == 'shencaozuo'][0]
        attitude4 = [i.get('count', 0) for i in json_data.get("attitude") if i.get("id") == 'suanle'][0]
        item = [title, media, str_date, readCount, replyCount, popCount, attitude1, attitude2, attitude3, attitude4,
                comment_url]
        crawled_num_mayi_data += 1
        print('============================================================')
        print(item)
        await wirte_demo_mayi_data(item)


async def data1(start_day):

    mysqlobj = Pmysql()
    conn = await Pmysql.getconnection()
    mysqlobj.connection = conn

    r2 = await mysqlobj.query(
        f"SELECT title, REPLACE(SUBSTRING(link,71),'&hasSpace=NO','') as link,media,str_date FROM cx0308 WHERE str_date  BETWEEN {start_day[0]} AND {start_day[-1]} AND post_type = 10")
    return r2

    conn.close()


async def data2( end_day):
    mysqlobj = Pmysql()
    conn = await Pmysql.getconnection()
    mysqlobj.connection = conn

    r3 = await mysqlobj.query(
        f"SELECT  title, REPLACE(SUBSTRING(link,71),'&hasSpace=NO','') as link,media,str_date FROM cx0308 WHERE str_date BETWEEN {end_day[0]} AND {end_day[-1]} AND post_type = 10  ")

    return r3


async def wirte_demo_mayi_data(item):
    # 异步方式执行with操作,修改为 async with
    with open(f'{current_month}蚂蚁财富数据.csv', 'a', encoding='gb18030', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(item)
        print("数据写入成功")


async def main_get(start_day, end_day):
    result = await asyncio.gather(data1(start_day), data2(end_day))  # 子生成器
    all_result_data = list(itertools.chain(*result))

    return all_result_data


def quchong_mayi():
    print(f'{current_month}蚂蚁财富数据.csv','正在统计处理...')
    a_dict = set()
    file = csv.reader(open(f'{current_month}蚂蚁财富数据.csv', 'r', encoding='gb18030'))
    aa_list = [tuple(item) for i,item in enumerate(file) if i !=0]
    for item in aa_list:
        a_dict.add(tuple(item))
    c = sorted(a_dict, key=aa_list.index)
    d_dict = {}
    csvfile = open(f'{current_month}蚂蚁财富数据统计数据.csv', 'a', newline='')
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    line = ['标题', '发布日期', '财富号', '阅读数', '点赞数', '评论数', '加油数', '笑出声', '神操作', '酸了',
            '阅读总数', '点赞总数', '评论总数', '加油总数', '笑出声总数', '神操作总数', '酸了总数', '网址']
    spamwriter.writerow(line)
    for title, media, str_date, readnumCount, popCount, replyCount, attitude1, attitude2, attitude3, attitude4, link in c:
        d_dict.setdefault(media, []).append((
        title, str_date, media, readnumCount, popCount, replyCount, attitude1, attitude2, attitude3, attitude4,link))
    for key, vlaue in d_dict.items():

        k, j, p, t1, t2, t3, t4 = [[] for _ in range(7)]
        for info in vlaue:
            q, w, e, r, t, y, u = info[-8:-1]
            k.append(int(q)), j.append(int(w)), p.append(int(e)), t1.append(int(r)),
            t2.append(int(r)), t3.append(int(y)), t4.append(int(u))
        k1, j1, p1, t5, t6, t7, t8 = sum(k), sum(j), sum(p), sum(t1), sum(t2), sum(t3), sum(t4)
        for info in vlaue:
            info = info[:-1] + (k1, j1, p1, t5, t6, t7, t8, info[-1])


            spamwriter.writerow(info)
    csvfile.close()
    print(f'{current_month}蚂蚁财富数据', '统计结束.')
    # with open('蚂蚁财富数据统计数据.csv', 'a', newline='') as csvfile:


def main_mayi_data(hao,start_day, end_day):
    start_time = time.time()
    print('正在读取数据,请销等........')
    csvfile = open(f'{current_month}蚂蚁财富数据.csv', 'w', newline='')
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    line = ['标题', '财富号', '发布日期', '阅读数', '点赞数', '评论数', '加油数', '笑出声', '神操作', '酸了',
            '网址']
    spamwriter.writerow(line)
    time.sleep(0.5)
    csvfile.close()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main_get(start_day, end_day))
    semaphore = asyncio.Semaphore(80)

    if hao == '号':
        tasks = [asyncio.ensure_future(detail_data_mayi(title, link, media, str_date, semaphore))
                 for title, link, media, str_date in result if hao in media]
    else:
        tasks = [asyncio.ensure_future(detail_data_mayi(title, link, media, str_date, semaphore))
                 for title, link, media, str_date in result if '号' not in media]
    tasks = asyncio.gather(*tasks)

    loop.run_until_complete(tasks)
    end_time = time.time()
    print('采集已用时间', end_time - start_time, '总共采集条数为', crawled_num_mayi_data)
    print('正在统计....')
    time.sleep(1)
    quchong_mayi()
    time.sleep(1)
    print('正在采集个人主页数据...')
    main_user()

#######################################################################
'财富号用户个人采集数据...'


async def resquest_user(resp_url, semaphore):
    split_url = resp_url.split("&")
    # print(split_url)
    c1 = split_url[0].split('?p=')[-1].replace('=', '').replace("/", "%2F").replace("+", '%2B')
    c2 = split_url[1].split('s=')[-1].replace('=', '')
    c3 = split_url[-1].split('c=')[-1]

    forever_url = "https://mobilegw.alipay.com/mgw.htm?operationType=alipay.mfinsnsprod.user.getUserProfileHTMLV3&requestData=%5B%7B%22encodeUrl%22%3A%22https%3A%2F%2Frender.alipay.com%2Fp%2Ff%2Ffd-j1xcs5me%2Fprofile-share.html%3Fp%3D{}%3D%26s%3D{}%3D%3D%26v%3DA1%26c%3D{}%22%7D%5D&_=1600843464871&callback=Zepto".format(
        c1, c2, c3)
    html = await fetch(forever_url, semaphore)
    return html


def detail_user_(task):
    html = task.result()
    user_pattern = re.findall(re.compile(r"Zepto\((.*)\)"), str(html))[0]

    user_data = json.loads(user_pattern)

    user_result = user_data.get("result").get("secuUserVo")

    user_name = user_result.get("nick")

    desc = user_result.get("desc")  # 大V描述
    certificated = user_result.get("certificated")  # 是否认证
    starredCount = user_result.get("starredCount")  # 关注
    followerCount = user_result.get("followerCount")  # 粉丝
    popCount = user_result.get("popCount")  # 被赞数
    rewardCount = user_result.get("rewardCount")  # 被悬赏数
    gmtCreate = str(user_result.get("gmtCreateLong"))

    if gmtCreate.strip() == '0':

        otherStyleTime = ''
    else:
        gmtCreate = gmtCreate

        timeArray = time.localtime(int(gmtCreate[:-3]))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    if '号' in user_name:
        item = [user_name, certificated, desc, starredCount, followerCount, popCount, rewardCount, otherStyleTime]
        spamwriter.writerow(item)
        print(f"{user_name}>>>>>数据写入成功")


def main_user():
    global spamwriter
    csvfile = open(f'{current_month}蚂蚁个人主页数据.csv', 'a', newline='')
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    line = ['财富号', '是否认证', '描述', '关注数', '粉丝数', '被赞数', '被悬赏数', '入驻时间', ]
    spamwriter.writerow(line)
    all_urls_data = [
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/DeljN9ifz/EgkCcjNTNNPY=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=edd995dc2796f6688328e9801bf4ad91',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/GrJl609rAfpwKGflX5KM6M=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=54dda7e305b38c97ea7f57a3c5d8e973',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/NfC/Zam+a3O6y2JSeoOwd4=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=57f6518063a585abf470cca062a8943a',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/C1GTgDRHOwSnRQOco+DHeQ=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=8c97331bf3ffc5b5ae6525d33c59c09a',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/Pp3j53O9WVX5ShbK/BLsI8=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=3bcff74d7936dda3e9c54cd38470af41',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/PT29BEViZ2ZgCjqweGUsIU=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=d38f1aae9658513d1d9719baf95b1e17',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/OTA3NMuHNXou//puBC8lUw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=715027b9d65384d8d2dc09ec1ea4a28d',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/PWtU/+hh4ZVqKGZWHSpkjQ=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=536367f417f96bcfc0c11818dae1f2ec',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/K6HUG+RMaVSY1sg+aP/sYw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=eb620209cc0fc21bf1b0d9fc3e9ade83',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/FS4i3yykhSmUcK5RfbqXzU=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=230252b634a16d81bf850ccfaaec8aea',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/GJdKqrrxiNdEUS9BN5ACoo=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=9e48fad82e4afde0f9716ebdede70929',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/LpdPtRD8NgB4DPU8Y9TGf4=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=eec5511c3f207e35dc468ba18f3be135',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JA5dFkPLzelI+lfMXJgL4k=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=686fa13acfeccabd4a1547c4f7a5785b',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/DbawXdvt99wDCrJeYjAFcs=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=f0feb30934c4c30ca810e777f6d0e61f',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/HqW39VtoPnoR6g2YA/HBT4=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=102fef15fa893224f1bbb0486c403482',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/IEFZqdAmKwJyXWxcpSuIoY=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=34cc0f031e8d941bd8dc82781aba5ef0',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/GoIq48Kd/IMJPD9oR41Shc=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=afc426a5e1404308e962b3dd18d5f49a',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/HMDETg2av6ZLqF8UdEfDfk=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=02ff6cb8031a2b94fbfcbedc0cf5dbe9',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JwOH3PKy8BCOI0gk7NL3Mo=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=d8b9414a74aaec7a8f740f28fc79c513',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/HOPIe7eadue/3zWz4lo6FQ=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=5bd84bc671473e4579bc5fe06f793a16',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/EqVQZKcIZUvOtdQArGoxFM=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=78125e0ae5610b39cef0633b5e6e55f0',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/EqFFJw9E0N/kynNBJ60fmw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=22f398e563d11c6121ad3ac45a1ee61d',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/Ocm4LgMu8GUCn3mliGEDJo=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=7d4cfca3e349a39418b596148a6a8fb5',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/PeCArNGP0uPpokP4u1PQA8=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=7126a6caffcec9ee4f701b77dc33d6ca',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/GQ5dZ1HnPPif2rJNEnct0k=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=53944aacb31b234fe65e53ae79edbd7e',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/MqN+rmEtBa86JNAVBpbrIs=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=5d570876a6de3dd2df8ac7af7de30797',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JGm+1Q8I4DoFMRHW2oQSA8=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=085426c72c9ec5abc938e629393f98a5',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/B+wedrH+1hA+uIzQUMrDy8=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=e074b3713d4276c25f8b54157f054c3f',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/PIbw0KHgb6YjWFGOeGgTtY=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=9804ac77363ddda76674db27d410e5c2',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/CDypwidAWrfOsBpCBl0sVU=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=53eda253c500f33d96a75839a85cb7ab',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/DhZHYrRJbPDJOEPcdsCO6Q=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=90cea8462a732ac690c79e401621bb47',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/C5unWtwDTGcD0/HW7iQl4c=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=5ffde510c887da653984197c9bafc598',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/NpzwMGLjiUy4y8D9OktXPs=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=fa3222c866a51269e41da40843472acd',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/LNSdqqItW/7NJCRal2tihw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=fc61a3ff6c2f2a50212936c190297b98',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/IaWuFTIU1lPATcabVCYLnM=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=7d3a7ffa97e872b79402f7a40d71a903',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/DcgqKWq5pE62EAOAzrouqY=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=490644d987d81db4176187c1cdc5b38c',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/FNeEQLr2bnvI+L+lZix9kE=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=e9b870d53b28a0309f5c72dcfa7f09d2',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/IN5X8ogg2Re0hWgoREhzsc=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=8035a75b84ffcae652afe22b2a894355',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/MbcmSsgo5qHAcuhWBE7CR8=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=bc886690d38241aa539cfc3472f60156',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/BWoais5mOMXtcIqurA0sRw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=defb6900b6a0c79268df5f98605424cc',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/DEzabu+4XPBxUnVGGlASUU=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=6d557202e2bc69d3243bab0097622f1c',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/GTFQTkmtXDyrxI7xQwPRpQ=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=88ea52d33525eaebc08a459e4cdb1106',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/GMEwvYCqWVF0bh3ErhJbV4=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=bab1cee4a79ce6343c6242fe691fdc8f',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JL9QBJzybwehtrbvx2yGjw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=cbe939792829d44d30bc11dd4dd9dfc1',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/MxgKqiR0o3KOO7pH2BgxVw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=34c07c490fac9211e443f6f8f03f1ac1',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/H2ugXPakkfAL0R2D8QRC7Q=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=0de06bb90a851a288dddc0b7de8de078',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/MOZiNuMGkFYuzl39INp6yg=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=a439fbd168c1ea917da6791e07177cfd',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/Ha0qDnZd4QvVgLNhXK7r4w=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=421a34dc0e16a5d704daa221fa683131',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/ISAIOO8O9PD9jYVV8lHFi4=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=0a93d0bafb80e76c576313deb787cb9c',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/LwoyBFdXNJdLBbJD5WHr1o=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=15f6acd90bd1f72a9c5466c4b6597041',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/OJ4jjw3namTVMGkn8tlUPU=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=937d4c2e6ea2b598ef96dd72354aef95',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/IfqUX0neUCv0za/GT+DVVM=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=09904c2e9888d14ec4245e4feb609a7b',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/NxbiZqUp1Afb6jo7k0p40w=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=315c2ab63cd797a104995ab6b1f5e657',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/DBf47mXK+YpdFs4VlVLSSs=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=70083d6b00dcb0f3320237b950786a9c',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/FnFyS9jdjLRSBc7bQBS4Zo=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=55cac065e126125deaf1374300809acb',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/NPeKV8oUt7sBM5QBhNzyZA=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=92e1333442ac3ecb66acbb2db5da5c62',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/FP8IQfAXiBX099y1VY+kEg=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=2d5f1dd56db7d1a16c74e900fdb155aa',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/DBeh/FEQDH7Y4XDBnLkMBw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=fe5cb799df702339e9c1d25a2538d7bc',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/MYgx7Cc/oC7Dw53+DAdzx0=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=76634620f98680e38f91332c07184740',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/NGwN6ZJRFOT33agKqb+Zoc=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=0eee21f184557343cc58912a02dfff20',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/EKIDEyziLCMNstDz3YcAFA=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=2373328b144820866f2867d0e1234c97',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/AOHzgBZfDb5F1TodhkgyAk=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=f813319e21ac912dfa08a39b656fe9a1',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JR8Jr/ns/q74TEx7Rj4kgE=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=a40f4d9e4e672de726047e6ba901f56e',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/OnSLnGb9xjlOovNLLAObqs=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=1d083fc783d30f17237c8db06903a272',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/OOaNZMqeEE22mBFVvAXlls=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=04b23256c0017c7503f9b7f56cd795ec',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/DOkYf+TEGAu0WClTnBj2O4=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=b0f03eb5b24e182f53ba77ef13aea677',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/FecZOtCUvk9DnUyOXia514=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=4c5e7e2560ca41c12444b9f64f2d7d9b',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/LpzH+mKYrKvmDRRKhCORis=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=6e3695a62c882b783860b346037269e8',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/PtX0YXM7sCtVdvtMWZpiGM=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=c15db69e45027b17881f19c575a979b1',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/KlMlvGoWLQEQ9xk3iJ5sHY=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=793eb65b07badb3ef5c35a04bd34738b',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JbU5EZgmQraacU1QoPfKCw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=0138aec5b260ab11c752d9d65c533d27',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/NlcdDcrRXpFAnfg+0ky4p8=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=469162b53f2c6c3b136303037ed05304',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/HMLr5iWv+/OZMMD1jpSJY0=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=e1a2c29975cf9a80d6f345417854edc0',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JfnwfeWUeym/8CiR74JCAM=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=1bb8d466e36b1b8ab50f5e5874c6a71e',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/Fb0lqSWMpp4aDVSAkEasIg=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=2dfb00ab0cccc13e734504dfcb55b1dc',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/BcHhlmTkAmbjX+tc+R9Tbc=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=538977b375110ace7e00cca0e17fbb28',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/I8NVAVV2CjkZdh9LfgwTc0=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=d8bc2080621fba4af1873bde72d0aa6c',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/FpkkSdBV6XSlp8Ll3WUG00=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=11877a6ac9ef8373cebdb88fb848f9e6',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/IqaJVVO4n4CrDs+dLIst/8=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=a34b79e5967dd23f5ddc778274e065ae',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JF3eC0Z3/TkGGcH5D9r27I=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=8478a42f1f46659ac6f57bd583878ef5',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/MVEALtBto+90qqTZ2LuATM=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=03c8f106c30fcc993c01fbb49b8789c0',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/D7EfbsPUoMUnYOc8LaVkpI=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=a54722c0cf0f1785a2313a5a430f5fde',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/NNhizC2PQTI6BovAd8Kz7w=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=ab37833ea6007428997696ad0f61e839',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/CtO7NyiW5QhUcps6n9pDA4=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=20793529c9ef8cabca79a7d17d432b47',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/MZJMtEVCX7aBipfPNT9T0Y=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=a130bec53b1b12336022cb84445a30bd',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/DeljN9ifz/EgkCcjNTNNPY=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=edd995dc2796f6688328e9801bf4ad91',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/FnFyS9jdjLRSBc7bQBS4Zo=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=55cac065e126125deaf1374300809acb',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/EKIDEyziLCMNstDz3YcAFA=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=2373328b144820866f2867d0e1234c97',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JfnwfeWUeym/8CiR74JCAM=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=1bb8d466e36b1b8ab50f5e5874c6a71e',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/EqVQZKcIZUvOtdQArGoxFM=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=78125e0ae5610b39cef0633b5e6e55f0',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/P9Dkl9WmmjdiD90jkBMAmc=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=a252b20cf77c74e26cac448470b60b77',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/OuvjAqf9Yitf01ki/A/sjw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=5c3f9172134901ecd8ab82283e89bca3',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/PnULfRBylC0Yxo9MQesoqE=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=0a2f45a260b520a25fa2ff8c33fa12f6',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/Ga1vQDNh0cZfkISgJcjkVg=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=85835a309d21a835d09c5bc1d0fa2f56',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/HSQ7wKDuM2k0uRRxVinDu8=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=4782953875540bf019cea20d8926655e',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/F+e5i+tf2ET6bsxvkHzQCw=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=53156a9d1b09ba97fd1213a6e1ccb74f',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/KqqciwVJTBFMn1SNU8kJXc=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=8c775c7d4cdafb8ac4af503fc286cfee',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/IczgxuWXCVAeEY/yLCa/oU=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=b9bbd47bd42dfd96c258e5abbf68cb63',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/E6ZbAwBcmRW2EhFVnYu6eM=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=117c6d3efac902bd394b965d802d2656',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/HWvr0Kwo4TNsIpttRjAuw8=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=228206d6f9c26df6bd51ad0cf73f29d5',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JkCgq+ShHD0yNzr7Q4MA70=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=915fef022a602de12c3db31382c180ec',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/CIEqVUh8ooWyEmBieuQk6E=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=201f3caaaacc38e196e7aca935bece00',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/E5+MCpk+QVYEwxxMNyYMAs=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=af4fcf1dbe2557d53c95a7b2b8df035d',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/DueMR9VIVQ+vBeOlckVybo=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=7cff7c8938b15a1e3cb08d77ad75ff8f',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/JrfzBqo3IN0okVi1hMdfDA=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=076a42b18d66d322bf58af9f250b2f1f',
        'https://render.alipay.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/Bd4H5Y/eHrSs5/ZsASDEyI=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=25045dabf988a71d37c59aba786945bc',
        'https://now.5ylhci.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/KM6XP6U1uXg99MKJoBlB18=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=a0105ce1b1abbf7ca22af8126ede3e6a',
        'https://now.5ylhci.com/p/f/fd-j1xcs5me/profile-share.html?p=xzBtqDr27isQTBITxlfxGfZ/jrIrmPlQ5Nh11RU/vFIN+JP9Vt2NEEzelwf/fBiATLhmgELuxaIJoOWcOqtL/OJ/H8i/sjEUY4xTHvAqXic=&s=YaqZnA16rNN2elNumX7hVg==&v=A1&c=3c9525f4ca7af035fea9d1c791c62bd2']

    all_tasks = []
    semaphore = asyncio.Semaphore(40)
    for url in all_urls_data:
        task = asyncio.ensure_future(resquest_user(url, semaphore))
        task.add_done_callback(detail_user_)
        all_tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*all_tasks))


def weixin_main():
    import requests
    import pymysql

    dbhost3 = '120.26.106.222'
    dbuser3 = 'julai01'
    passwd3 = 'Sh51785136@sh'
    dbname3 = 'jijin'

    conn3 = pymysql.connect(dbhost3, dbuser3, passwd3, dbname3, charset='utf8')
    cur3 = conn3.cursor()

    sql = 'select sipder_code from spider_info where spider_name = "微信"'
    cur3.execute(sql)
    sigle = cur3.fetchone()

    print('sql输入列如:SELECT  DISTINCT b.post_id,a.`link`,a.media FROM cx0308 a INNER JOIN hisinfo_cx b ON a.`id` = b.`post_id` WHERE b.`post_type` =3 AND b.del_flag = 0 AND b.`str_date` BETWEEN 20200220 AND 20200229 AND b.`readnum` =0 order by a.media asc limit 1000')
    sqls = input('''请输入sql语句并\n以媒体order by进行排序\n必须select post_id,link,media,三个字段: ''')
    # sqls = '''SELECT DISTINCT b.id,b.`link`,a.media FROM `hisinfo_cx` a RIGHT OUTER JOIN cx0308 b ON a.`post_id`= b.`id` WHERE b.id > 19000000 AND b.`post_type` =3 AND b.str_date >= 20210509 AND b.content REGEXP '叶飞' AND b.content REGEXP '申万宏源|民生证券|恒泰证券|天风证券|易方达|博时|泓德|金信|公募基金|券商'  AND a.`readnum` =0 ORDER BY a.media ASC LIMIT 3000'''
    sql = '''{}'''.format(sqls)
    print('请等待,数据正在读取中.........')

    cur3.execute(sql)
    data_list = cur3.fetchall()

    if sigle[0] == '-1':
        input('有人正在使用...，请回车推出等待...')
    else:
        sql1 = "update spider_info set sipder_code = '-1' where spider_name ='微信'"
        cur3.execute(sql1)
        conn3.commit()
        vaild_num = 0
        invaild_num = 0
        all_data = 0
        for post_id, link, media in data_list:

            all_data += 1
            data = f"[[{post_id},'{link.strip()}','{media.strip()}']]"

            url = "http://192.168.0.39:9001/items/"

            payload = '{"sql":"%s"}' % data

            headers = {
                'Content-Type': 'application/json'
            }
            print(payload)

            response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'))

            response_json = response.json()
            print('============================================================')
            print(response_json)
            if response_json.get("readnum"):
                vaild_num += 1
            else:
                invaild_num += 1

        dall_tetx = {'采集总数为': all_data}
        print(dall_tetx)

    sql2 = "update spider_info set sipder_code = '1' where spider_name ='微信'"
    cur3.execute(sql2)
    conn3.commit()

if __name__ == '__main__':

    print('选择你采集的平台数据：1为蚂蚁，2为微信，3为头条')
    platform = input('请选择平台并按回车:')
    if platform == '1':
        print('选择你采集蚂蚁财富号或大V个人号：1为蚂蚁基金公司财富号，2为蚂蚁个人大V号，')
        mayi_platform = input("请输入选择并按回车:")
        now = datetime.now()
        print('输入的月份实例支持跨年份：20200401-20210531')
        input_month = input("请输入需要采集的月份:")
        start_month = input_month.split('-')[0]
        end_month = input_month.split('-')[1]
        #
        # last_month_start = datetime.strftime(datetime(now.year, int(start_month), 1), '%Y%m%d')

        # last_month_end = datetime.strftime(datetime(now.year, int(end_month), 31), '%Y%m%d')

        last_month_start = start_month
        last_month_end = end_month

        import datetime


        def getEveryDay(begin_date, end_date):
            date_list = []
            begin_date = datetime.datetime.strptime(begin_date, "%Y%m%d")
            end_date = datetime.datetime.strptime(end_date, "%Y%m%d")
            while begin_date <= end_date:
                date_str = begin_date.strftime("%Y%m%d")
                date_list.append(date_str)
                begin_date += datetime.timedelta(days=1)
            return date_list


        day_list = getEveryDay(last_month_start, last_month_end)
        if len(day_list) % 2 == 0:
            num = int(len(day_list) / 2)
        else:
            num = int(len(day_list) / 2) + 1

        start_day, end_day = [day_list[i:i + num] for i in range(0, len(day_list), num)]
        print(start_day, end_day)

        if mayi_platform == '1':
            hao = '号'
            main_mayi_data(hao,start_day, end_day)
        elif mayi_platform == '2':
            hao = '非号'
            main_mayi_data(hao,start_day, end_day)
    elif platform == '2':

        print('使用微信前，联系打开程序.')
        weixin_main()
    elif platform == '3':
        print('输入的月份实例支持跨年份：20200401-20210531')
        input_month = input("请输入需要采集的月份:")
        start_month = input_month.split('-')[0]
        end_month = input_month.split('-')[1]
        # import os
        # print('数据正在读取中....')
        # os.system("python toutiao_data.py")
        import csv
        from datetime import datetime, timedelta
        import json
        import os
        import re
        import time
        import requests
        import aiohttp
        import asyncio
        import async_timeout
        from lxml import etree
        from urllib.parse import urlencode
        import aiofiles
        from retrying import retry
        now = datetime.now()
        current_month = datetime.strftime(datetime(now.year, now.month, 1), '%Y-%m-%d 00:00:00')

        now = datetime.now()
        currentday = datetime.strftime(datetime(now.year, now.month, now.day), '%Y%m%d')

        csvfile = open(f'{currentday}头条号个人主页数据.csv', 'a', newline='')
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        line = ['标题', '发布日期', '头条号', '阅读数', '点赞数', '评论数', '网址']
        spamwriter.writerow(line)
        csvfile.close()
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

                   # 'Cookie':'passport_csrf_token_default=ab3715eef42f24ce85eba051279b4a8f; ttwid=1%7CEQqaQRGYqJHbM6vjddSmseATuLjWIh4Z9_nFPJ-svOk%7C1622256706%7C1f696e3b542d66b8a943a7f0cb6b99906dfe8c26d74a81bdfbbf23c0eb43c2a5; WIN_WH=352_546; PIXIEL_RATIO=1.5; FRM=new; tt_webid=6951613006950188581; s_v_web_id=verify_cbff3704ff2a8f82867b9ac9bb74260f; _S_WIN_WH=1280_562; _S_DPR=1.5; _S_IPAD=0; MONITOR_WEB_ID=6951613006950188581',

                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
                   }


        async def check_title(title, content_url):
            if '/w/' in content_url:
                try:

                    title = re.sub(r'\s+', '', title)
                    if any(i in title for i in ['?', "!", '？', '！', '！ ']) and '。' in title:
                        gap_word1 = [i.span() for i in re.finditer('？|\?|！|!|？|！ ', title)][0][0]
                        gap_word2 = [i.span() for i in re.finditer('。', title)][0][0]

                        if gap_word1 <= gap_word2:
                            titles = re.split("？|\?|！|!|！ ", title)[0]
                        else:

                            gap_word1 = [i.span() for i in re.finditer('，|， |，|,', title)][1][0]

                            gap_word2 = [i.span() for i in re.finditer('。', title)][0][0]
                            if gap_word1 < gap_word2:

                                titles = ','.join(re.split("，|， |，|,", title)[:2])
                            else:
                                titles = re.split('。', title)[0]
                    elif any(i in title for i in ['，', ",", '， ']) and not any(
                            i in title for i in ['?', "!", '？', '！', '！ ']) \
                            and '。' in title:

                        gap_word1 = [i.span() for i in re.finditer('，|， |，|,', title)][0][0]

                        gap_word2 = [i.span() for i in re.finditer('。', title)][0][0]
                        if gap_word1 < gap_word2:

                            titles = ','.join(re.split("，|， |，|,", title)[:2])
                        else:
                            titles = re.split('。', title)[0]


                    else:

                        if '。' not in title:
                            title = re.split(',|，', title)[:2]
                            titles = '，'.join(title)
                        else:
                            titles = re.split('。', title)[0]
                except:
                    titles = title[:50]


            else:
                # title = ''.join(re.findall(r'[^\x00-\xff]|[0-9]{5}', title))
                if '。' in title and '】' not in title:
                    titles = title.replace('&quot;', '').split('。')[0]
                # elif '】' in title:
                #     titles = title.replace('&quot;', '').split('】')[0] + "】"
                else:
                    titles = title.replace('&quot;', '')
            return titles


        NETWORK_STATUS = True


        def get_proxy():
            global proxy
            PROXY_URL = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&groupid=0&fetch_key=&time=100&qty=1&port=1&format=json&ss=5&css=&dt=0&pro=&city=&usertype=4&et=1'
            # PROXY_URL = 'http://tz2.zhangyupai.net:5010/get/'
            try:
                if NETWORK_STATUS:

                    response = requests.get(PROXY_URL)

                    if response.status_code == 200:
                        time.sleep(0.8)
                        proxies = str(response.json().get("data")[0].get("IP")) + ':' + str(
                            response.json().get("data")[0].get("Port"))
                        # proxies = response.json().get("proxy")
                        proxy = 'http://' + proxies
                        return proxy
                else:
                    proxy = proxy
                    return proxy
                # else:
                #     proxy = proxy
                #     return proxy
                return None
            except ConnectionError:
                return None


        async def start_fetch(session, url, media, semaphore):
            global NETWORK_STATUS

            async with semaphore:

                await asyncio.sleep(0.6)
                while True:
                    try:
                        async with session.get(url, headers=headers, timeout=8) as response:
                            result = await response.text(encoding='utf-8')
                            if any(i in str(result) for i in ['max_behot_time', '粉丝', 'group_source']):

                                return result
                            else:
                                proxy = get_proxy()
                                NETWORK_STATUS = False

                                async with session.get(url, headers=headers, proxy=proxy, timeout=8) as response:
                                    result = await response.text(encoding='utf-8')

                                    if any(i in str(result) for i in ['max_behot_time', '粉丝', 'group_source']):
                                        NETWORK_STATUS = False
                                        return result
                                    else:

                                        NETWORK_STATUS = True
                    except Exception as e:
                        NETWORK_STATUS = True
                        print(url,'请求超时，再次发送请求')


        now = datetime.now()
        current_months = datetime.strftime(datetime(now.year, now.month, now.day), '%Y%m%d')

        @retry(stop_max_attempt_number = 5)
        async def parse_details(session, url, media, id_, semaphore):
            data = json.loads(await start_fetch(session, url, media, semaphore))

            success = data.get("success")
            if success:
                all_data = data.get("data")
                group_source = all_data.get("group_source")

                if group_source == 5:  # 微头条
                    thread = all_data.get("thread").get("thread_base")
                    content = thread.get("content")
                    title = thread.get("title")
                    create_time = thread.get("create_time")
                    time_ = time.localtime(int(create_time))
                    time_ = time.strftime('%Y-%m-%d %H:%M:%S', time_)
                    media = thread.get("user").get("info").get("name")
                    source_url = 'https://www.toutiao.com/w/a{}/'.format(id_)
                    read_count = thread.get("action").get("read_count")
                    digg_count = thread.get("action").get("digg_count")
                    comment_count = thread.get("action").get("comment_count")

                elif group_source == 23:
                    comment = all_data.get('comment').get('comment_base')
                    title = comment.get('content')
                    content_ = all_data.get('comment')
                    if 'origin_thread' in content_:
                        content = content_.get('origin_thread').get('title')
                    elif 'origin_group' in content_:
                        content = content_.get('origin_group').get('title')
                    else:
                        content = ''
                    # content = title + content
                    create_time = comment.get('create_time')
                    time_ = time.localtime(int(create_time))
                    time_ = time.strftime('%Y-%m-%d %H:%M:%S', time_)
                    media = comment.get("user").get("info").get("name")
                    source_url = 'https://www.toutiao.com/w/a{}/'.format(id_)
                    read_count = comment.get("action").get("read_count")
                    digg_count = comment.get("action").get("digg_count")
                    comment_count = comment.get("action").get("comment_count")
                else:
                    title = all_data.get("title")
                    # content = all_data.get("content")
                    publish_time = all_data.get("publish_time")
                    time_ = time.localtime(int(publish_time))
                    time_ = time.strftime('%Y-%m-%d %H:%M:%S', time_)
                    media = all_data.get("detail_source")
                    source_url = 'https://www.toutiao.com/i{}/'.format(id_)
                    read_count = all_data.get("impression_count")
                    digg_count = all_data.get("digg_count")
                    comment_count = all_data.get("comment_count")

                title = await check_title(title, source_url)
                return title, time_, source_url, media, read_count, digg_count, comment_count


        crawl_num = 0


        async def wirte_demo(item):
            global crawl_num
            with open(f"{currentday}头条号个人主页数据.csv", "a", encoding="gb18030", newline='') as fp:
                write = csv.writer(fp)
                write.writerow(item)
                crawl_num += 1
                print("采集数据写入成功")


        async def download2(session, token, media, semaphore):
            max_behot_time = '0'
            change_flag = False
            while True:
                url = f'https://www.toutiao.com/toutiao/api/pc/feed/?category=profile_all&utm_source=toutiao&visit_user_token={media}' \
                    f'&max_behot_time=0'
                path1 = 'all_js_code.js'
                sign = os.popen(
                    'node {path1} {url} {cookies}'.format(path1=path1, url='"' + url + '"', cookies='"' + '' + '"'))
                sigin = sign.read().strip()
                params = {'category': 'profile_all',
                          'utm_source': 'toutiao',
                          'visit_user_token': token,
                          'max_behot_time': max_behot_time,
                          '_signature': sigin,

                          }
                index_url = 'https://www.toutiao.com/api/pc/feed/?' + urlencode(params)

                html_json = await start_fetch(session, index_url, media, semaphore)

                await asyncio.sleep(0.5)
                all_data = json.loads(html_json).get('data')
                for item in all_data:
                    if 'group_cell' in item:
                        id_s = item.get("base_cell")
                        if id_s:
                            created_time = id_s.get("log_pb")
                            if 'create_time' in created_time:
                                created_time = created_time.get("create_time")
                                Other_time = time.localtime(int(created_time))
                                post_time_s = time.strftime('%Y%m%d', Other_time)
                                if post_time_s >= current_month:
                                    id_ = id_s.get("log_pb").get("logpb_group_id")
                                else:
                                    id_ = None
                            else:
                                raw_data = json.loads(item.get("stream_cell").get("raw_data"))
                                stream_cell = raw_data.get("origin_thread")
                                answer = raw_data.get("content")
                                if stream_cell:
                                    created_time = stream_cell.get("create_time")

                                elif answer:

                                    answer_time = [answer.get("answer") if 'answer' in answer
                                                   else answer.get("question") for i in answer]

                                    answer_time = answer_time[0].get('create_time')
                                    Other_time_answer = time.localtime(int(answer_time))
                                    created_time = time.strftime('%Y%m%d', Other_time_answer)
                                else:
                                    created_time = raw_data.get("comment_base").get("create_time")

                                if '内' in created_time or created_time >= current_month:
                                    id_ = id_s.get("log_pb").get("logpb_group_id")

                                else:
                                    id_ = None
                    else:

                        id_ = item.get("item_id")

                    if id_:
                        index_url = 'https://m.toutiao.com/i{}/info/'.format(id_)

                        title, time_, source_url, media, read_count, digg_count, comment_count = await parse_details(
                            session, index_url, media, id_, semaphore)
                        datetime_str = str(time_).split(" ")[0].replace("-",'')
                        if str(datetime_str) <= str(start_month):
                            change_flag = True

                        elif str(start_month) <= str(datetime_str) <= str(end_month):
                            await wirte_demo([title, time_, media, read_count, digg_count, comment_count, source_url])
                            print('============================================================')
                            print(title,time_,media, '数据正在采集.........')

                if change_flag:
                    break
                next_page = json.loads(html_json).get("next").get('max_behot_time')
                max_behot_time = next_page


        if __name__ == '__main__':
            words_str = '''易方达基金 MS4wLjABAAAAUFucNRxsfYdNeglMZ3gYWqvhYCBGsgH9O3POREhxl7NUKm6ZHam_qfUc1yITPgSM
易方达投顾 MS4wLjABAAAAZl0bKzoY_AAana5kxZodEYL9mNjhcZsIrYprSf0Ksrl0EThDtRB6hyekw3elp16-
汇添富基金 MS4wLjABAAAAkyD7aY2X2h-4nk-6qASPBMY2ib_ghTpcfVwqW6cjVrq3-vc5cVpSJ4GfEP1t6Hml
华夏基金 MS4wLjABAAAACEBmDJO7OUyK7hZ7SYHGRQpKOFFwwfIrSAxELEUznIY
广发基金 MS4wLjABAAAAorM_WgMzlu9gjPKdxlD8AIk_f6ZmPw9oxv-Cm8mG54k
南方基金 MS4wLjABAAAAyRBDxb6W6hvQZ8Bf0xalLWzTurIRITIBbidtY_MtVZE
嘉实Harvest MS4wLjABAAAAXhc0ANLC1KPqNv5NHLm7R_BXgRU53i82zTLcQT2-a-w
富国基金 MS4wLjABAAAAax3JOanR3hLI9ehq0QqsqBaFzAjuZ-yqiSSDZGHeOT4
嘉实基金 MS4wLjABAAAAEcl6y-YFz8a8ncFOZrGU23SM4uGJi4fC9s_PLIQiptQ
博时指慧家 MS4wLjABAAAA1oce89McJCWL4O-ju4xulH6uIHdLL3woaG_s7CWQ-0M
博时基金 MS4wLjABAAAAUatp3TgYP60HawPJX9TQT7XHj4Z4QLtzpED-543kiQI
博时宏观 MS4wLjABAAAApEJrGXeP8MkTZTFZa2f6b3d9hHJxnYVOEloUYktXr0qfbGZwPWT9pDPJLlDZinnX
博时权益 MS4wLjABAAAAtn0ournl8SB-kmT9pEWV2Sfs8Pxtn8E9YCWuP5NnVQc
博时固收 MS4wLjABAAAAL2-PWt59CRHmUBZ6NlBpueUMX2uU2I-xIeHBGgRaFdZ-FsPtcnsfedKmZiBmm_N5
博时养老 MS4wLjABAAAAVviiMWXylIu7RL757TbHdQluX2d-oXgRh4YYRVT37232scarvD2TsdUdN0ljMO3Y
博时FundTalk MS4wLjABAAAAK85saMYFuSDmzhYHgIu4A1-blcFYtoE2l31lg8UDoiE
招商基金 MS4wLjABAAAAT66QPei2e4eIAgRJmuVW--u2d1Hj7qLAbGB4aILdSZ0
鹏华基金 MS4wLjABAAAAjr9ycI8owWuDrqRW5OMKmmLP3e793sqZkCJ39MyboQ8
工银瑞信投教研习社 MS4wLjABAAAAqwCM50vVxThf1yLhhof8-EkEeHiNFW540JE-zzPlLCg
工银瑞信基金 MS4wLjABAAAAUJOgklR7-HJZSRLVJAwzOLNp8aU0ikXqisLt1WUGjGo
中欧基金 MS4wLjABAAAA_IZy3AxSox4hNxumisx0v8R0xc8YX0C9rz0M7ioxugg
中欧基金权益团队 MS4wLjABAAAAs4tlBcqOfFXyDVXyNPY5fPPvxIx07T2ZwLBCSFf_zN9hmA6DPHefc08JBdJ9-Kwf
中欧基金固收团队 MS4wLjABAAAAUpbr5xbtU1r60gPbNRiS5XyxORPuM6PLuQ-yR3KtBOo
中银基金 MS4wLjABAAAAXtMqSVHVMpWNeO3wyqQrHJbI1AduyrrgmZKvd6oeuTk
华安基金 MS4wLjABAAAADbb7Xxg7abW0GD7OYX11mkci8MVSt86R0kzOGuMnRIo
交银施罗德基金 MS4wLjABAAAAPdxxvDO0IBkT4kpCl_Hz6jmEkq7QHIr16lI2rqGcsxQ
兴证全球基金 MS4wLjABAAAACouiEpVnZBuaHBW3JYduqQF0j-blHk0UpPkkzeuGg54
国泰基金 MS4wLjABAAAAnqoPLpLrTxssDRHIGwtg0RMJFXgzuQRK-mbY5YLk4iiwMtZhpZVoiARFnrAbVlTd
景顺长城基金 MS4wLjABAAAAMlW3GeJAbI0VF6ZrLKtMSruc_xWKLFwOsegfrNZVHVo
银华基金 MS4wLjABAAAAGiDtKxdV1rCIsvsQ9P6TVOQ7Hon2gs_eDP2tzKdRsbJilicHLwEVhb2GKqLFwUPx
上海东方证券资产管理 MS4wLjABAAAA5e8TXpXXtqimXVbtvvlj62rbvzad1XBgMdf2SkHExNFQ5baRJyNiuAY26QsszdqG
农银汇理基金 MS4wLjABAAAAgO66gBtQ4JWh-CgAgeh9JT9-Ma2lAKERXJsmnW4NeeVj7WckvFaXa0xAN3ZqMEaX
建信基金 MS4wLjABAAAA92EHY5Ycc_m-MBfmI9TfLVVlgIeqr5wPK79bsG06OKM
平安基金 MS4wLjABAAAAhwc0oclOb3ZfIgHi7VznwNLvWWJUUYivcww7U5liHyM
永赢基金 MS4wLjABAAAAoZy5GgfknF1CKrdbrtygWMJg0Z24cay5VVYOfxhryUCHbEDmHxw2HvYeWM0e-Vhw
兴业基金 MS4wLjABAAAAxNls8VxvAEeWKcMg4S2MtEQRca3PKueOvuK2BtSLrpCV_WYBaaR3cPu8J14IXCu6
天弘基金 MS4wLjABAAAA1FxVsGrM4dz9mr0eKLRhY8OAXhiA40eBUdbqJ10-99Y
大成基金 MS4wLjABAAAAVTNLWjYQSJxPuhLrnh4dod5NeIzKD6r_v5QKxq3Mr-Q
华泰柏瑞基金 MS4wLjABAAAAGwmud-piWbz7tX9tOAJPy_5LrRzHVrkRND-7LRiXzYw
华泰柏瑞指数投资 MS4wLjABAAAAbRp1QJYmhYCypmAmLMCk3ozwD9nDECK9iR1_l6dmUTeXX9-DFmelKNqOZ_rN6QZa
万家基金 MS4wLjABAAAAbxUk8kVy0YR2q3lU103-9wg1o-Qrrtulid6JaFuGvBjSusIiUywGQUH87We6Mhcf
泓德基金 MS4wLjABAAAA0UaQwKHCh8dHfgtSZJFKntEmHb98rG6GwSXvY_JacMTYFTkZMhlp4R2N4vvMN4pf
华宝基金财富号 MS4wLjABAAAAVyhlJbxPRqH3rQHHlx2vQO2QGTs71QGGO7iy1XTKaZqJQJEqzwvw1399mFVbgu1C
浦银安盛基金 MS4wLjABAAAAT1hRGFIa-445HpnZTxH06EmMcxlGEpnNJpFsOgmPGPdYAMlRkrux-SteVQfkTNv4
中银国际证券资管 MS4wLjABAAAAPcfMHFjErSb0VSkvZgPXheZrV6rGIHJh4iEjo2eWQHsOJVYgvvz9HfZ6RIe8D7_-
中信保诚基金 MS4wLjABAAAATDCiLDpDRO22vNSnJY2RHA_vm8GyKrOrG6aAUKfcSwk
中加基金 MS4wLjABAAAAbIutuN8_fr15Ph0sIukhyE5JXsnUUeDwsAtnv2J7inQ
长城基金 MS4wLjABAAAA_07DxArKx5drhJDeBI7TiOtECmYhesUtSl_qHNAafjvf38lwgoV5Yj5GTRrDVbLl
银河基金 MS4wLjABAAAAAoY7W2es1yyMpgqVVpbgojMoLMRWAl0A9ihasUUIPyHRh-rp4qcJks24_AUqGc_B
融通基金 MS4wLjABAAAAnAIS97p4qNE87oHv3e-0uQkitfW5Mg4AHt9A-MnLoKJvuU12x147JRKfsMFLx9Q0
海富通基金 MS4wLjABAAAAusJgJtE9VN60P1qX8sRqeswkXObpsEMrWPyRME_ElkqSDHeGCeNMHeqclN1EMblo
诺安基金 MS4wLjABAAAAhuxpj7eNEg2C7jR3ErTFd0d93b88Jw-2EG2i3qa-SV8
上投摩根基金 MS4wLjABAAAAGm3fimrGCTOnzvM_ng1FWjBBTKmnteYsRdQXG-GCfN4GL26soDh1RVc9G110kr41
泰康资产 MS4wLjABAAAAx05iRC2r4toK945Ej0wYlEXcijYL7TfzbBaWfPHyomn431-4n0FI3UXrM2qKZwrY
前海开源基金 MS4wLjABAAAAbDxBepjYxkdd2uinBomPXuD5le7Qf7zSfBd5ojkNEwQ
国投瑞银基金 MS4wLjABAAAANNovMV3XhzYv3tWhibe22ZsReuht9aBtBnV0M9xoh14
长信基金 MS4wLjABAAAAgZP_SgjLohK6Dh0cMLQLjiPv_CtKSGQ5rOHBfmbimDY
中邮基金 MS4wLjABAAAAxgNg22P_w3B1FEAA6Eec7o8DKCggkEyHApTeGh6lZxg
富安达基金 MS4wLjABAAAAQYs25Wjjcurwxtx9atv2xBnJzwygjl5RULTBcnfABWg
国海富兰克林基金 MS4wLjABAAAAqkJVP-2MZVsBeyuZEhCReSjYFhg8fxKYnLmaoPrwpRc
新华基金 MS4wLjABAAAAX9tWVhsG6U8b8yXoi2uUwXfPZhf7_v6hLFsnlNMa3o1_ZhAyhE5N0dPTKCHXuzrH'''

            name_word_list = [i.split(' ') for i in words_str.split('\n')]
            print('正在读取数据,请销等........')
            start_time = time.time()
            loop = asyncio.get_event_loop()
            session = aiohttp.ClientSession()
            semaphore = asyncio.Semaphore(18)
            tasks = [asyncio.ensure_future(download2(session, name[1], name[0], semaphore)) for name in name_word_list]

            tasks = asyncio.gather(*tasks)

            loop.run_until_complete(tasks)

            loop.run_until_complete(session.close())
            loop.close()
            end_time = time.time()

            print('采集已用时间', end_time - start_time, '总共采集条数为', crawl_num)
    input('\n按回车结束程序..')
