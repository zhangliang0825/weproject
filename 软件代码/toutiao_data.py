import csv
from  datetime import datetime,timedelta
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

now = datetime.now()
current_month = datetime.strftime(datetime(now.year, now.month, 1),'%Y-%m-%d 00:00:00')

now = datetime.now()
currentday = datetime.strftime(datetime(now.year, now.month, now.day), '%Y%m%d')

csvfile = open(f'{currentday}头条号个人主页数据.csv', 'a', newline='')
spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

line = ['标题', '发布日期', '头条号', '阅读数', '点赞数', '评论数', '网址']
spamwriter.writerow(line)
csvfile.close()
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',

# 'Cookie':'passport_csrf_token_default=ab3715eef42f24ce85eba051279b4a8f; ttwid=1%7CEQqaQRGYqJHbM6vjddSmseATuLjWIh4Z9_nFPJ-svOk%7C1622256706%7C1f696e3b542d66b8a943a7f0cb6b99906dfe8c26d74a81bdfbbf23c0eb43c2a5; WIN_WH=352_546; PIXIEL_RATIO=1.5; FRM=new; tt_webid=6951613006950188581; s_v_web_id=verify_cbff3704ff2a8f82867b9ac9bb74260f; _S_WIN_WH=1280_562; _S_DPR=1.5; _S_IPAD=0; MONITOR_WEB_ID=6951613006950188581',

'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
}



async def check_title(title,content_url):
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
            titles  = title[:50]


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
                proxies =str(response.json().get("data")[0].get("IP"))+':'+str(response.json().get("data")[0].get("Port"))
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


async def start_fetch(session,url,media,semaphore):
    global NETWORK_STATUS

    async with semaphore:

        await asyncio.sleep(0.6)
        while True:
            try:
                async with session.get(url, headers=headers, timeout=8) as response:
                    result = await response.text(encoding='utf-8')
                    if any( i in str(result) for i in ['max_behot_time','粉丝','group_source']):

                        return result
                    else:
                        proxy = get_proxy()
                        NETWORK_STATUS = False

                        async with session.get(url,headers=headers, proxy=proxy,timeout=8) as response:
                            result = await response.text(encoding='utf-8')
                            print(result[-60:],22222211331,'{}ip更换......'.format(proxy),media)
                            if any( i in str(result) for i in ['max_behot_time','粉丝','group_source']):
                                NETWORK_STATUS = False
                                return result
                            else:

                                NETWORK_STATUS = True
            except Exception as e:
                NETWORK_STATUS = True
                print(e,'错误....')

now = datetime.now()
current_months = datetime.strftime(datetime(now.year, now.month, now.day),'%Y%m%d')

async def parse_details(session,url,media,id_,semaphore):
    data =  json.loads(await start_fetch(session,url,media,semaphore))

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

        title = await check_title(title,source_url)
        return title,time_,source_url,media,read_count,digg_count,comment_count
crawl_num = 0

async def wirte_demo(item):
    global  crawl_num
    with open(f"{currentday}头条号个人主页数据.csv","a",encoding="gb18030",newline='') as fp:
        write = csv.writer(fp)
        write.writerow(item)
        crawl_num +=1
        print("采集数据写入成功")

async def download2(session,token,media,semaphore):
    max_behot_time = '0'
    change_flag = False
    while True:
        url = f'https://www.toutiao.com/toutiao/api/pc/feed/?category=profile_all&utm_source=toutiao&visit_user_token={media}' \
            f'&max_behot_time=0'
        path1 = '_get_as_cp_signature.js'
        sign = os.popen('node {path1} {url} {cookies}'.format(path1=path1, url='"' + url + '"', cookies='"' + '' + '"'))
        sigin = sign.read().strip()
        params = {'category':'profile_all',
        'utm_source':'toutiao',
        'visit_user_token':token,
        'max_behot_time':max_behot_time,
        '_signature':sigin,

        }
        index_url = 'https://www.toutiao.com/api/pc/feed/?'+urlencode(params)

        html_json = await start_fetch(session,index_url,media,semaphore)

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

                title,time_,source_url,media,read_count,digg_count,comment_count =  await parse_details(session,index_url,media,id_,semaphore)


                if str(time_) <=str(current_month):
                    change_flag =True
                else:
                    await wirte_demo([title, time_,  media, read_count, digg_count, comment_count,source_url])
                    print(media,'号数据正在采集....')

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
    start_time = time.time()
    loop = asyncio.get_event_loop()
    session = aiohttp.ClientSession()
    semaphore = asyncio.Semaphore(12)
    tasks = [asyncio.ensure_future(download2(session,name[1],name[0],semaphore)) for name in name_word_list]

    tasks = asyncio.gather(*tasks)

    loop.run_until_complete(tasks)

    loop.run_until_complete(session.close())
    loop.close()
    end_time = time.time()

    print('采集已用时间',end_time-start_time,'总共采集条数为',crawl_num)