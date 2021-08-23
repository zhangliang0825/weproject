# coding: utf-8
import csv
import datetime
import re
import time

import demjson
from loguru import logger
import pymysql
from pyquery import PyQuery as pq
import requests
from wxpy import *

dbhost2 = '112.124.8.191'
dbuser2 = 'root'
passwd2 = 'Zycj@2020688'
dbname2 = 'tuisong'
conn2 = pymysql.connect(dbhost2, dbuser2, passwd2, dbname2, charset='utf8')
cur2 = conn2.cursor()

dbhost1 = '112.124.8.191'
dbuser1 = 'root'
passwd1 = 'Zycj@2020688'
dbname1 = 'news_caiji'
conn1 = pymysql.connect(dbhost1, dbuser1, passwd1, dbname1, charset='utf8')
cur1 = conn1.cursor()


with open('微信实时列表.csv','r',encoding='utf8') as f:
    all_media_crawled_list = [i.strip() for i in f.readlines()]




today = datetime.datetime.now().strftime('%Y-%m-%d')

logger.add(r'logtime.log',level="DEBUG",rotation='3 days')


# @logger.catch
def insert_data(id_data, title, content, times, original, author, query, meida_orig,contents_url, spider):

    data = {
        'title': title,
        'str_date': times,
        'digest': '',
        'media_orig':meida_orig,
        'content': content,
        'bizname': query,
        'content_url': contents_url,
        'biz': id_data,
        'readNum': '',
        'is_orig': original,
        'reporter': author,
        'spider': spider,
    }


    for i in range(1,10):

        try:
            insert_url = ' http://tz4.zhangyupai.net:81/mobile/import_wxpost.php'
            resp = requests.post(insert_url, data=data, timeout=7).text

            if '1' in str(resp):
                logger.debug((title,query,times,f'{i}次入库成功.....'))
                return '成功'
        except Exception as e:
            if e:
                return []

header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
get_token_url_weixin = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww3ab548a5b70fee4b&corpsecret=EsMQC6wclLWuHjpBxO6XDZpQH_WaL5f2f70ajsdcpRg'
get_toke_url_chat = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww3ab548a5b70fee4b&corpsecret=uTn2vEZe1iLXpvAcPV-35P9VvtYuRbiJHVKiU4kp34Q'

def get_token(tag):
    try:
        get_token_url = get_token_url_weixin if tag != '微信' else get_toke_url_chat
        token_response = demjson.decode(requests.get(get_token_url,headers=header).text)
        token = token_response.get('access_token')
        return token
    except Exception as  e:
        print(e)
@logger.catch
def send_data(title, media, r_time, link, content):
    if media !='微信':
        token = get_token(media)
        agentid = 1000002#微信公众号的id
    else:

        token = get_token(media)
        agentid = 1000003  # 微信聊天消息
    url = ' https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(token)

    data = {
        "touser": "@all",
        "toparty": "@all",
        "totag": "@all",
        "msgtype": "textcard",
        "agentid": agentid,#微信公众号发送id
        "textcard": {
            "title": "{}推送：{}".format(media, title),
            "description": "<div class=\"gray\">媒体：{}</div><div class=\"gray\">文章发表于：{}</div><div class=\"highlight\">"
                           "</div>摘要：{}".format(media, r_time, content),
            "url": "{}".format(link),
            "btntxt": "更多"
        }
        # "safe":0,
        # "enable_id_trans": 0
    }
    time.sleep(1)
    resp = requests.post(url, headers=header, data=demjson.encode(data)).json()
    if resp.get("errmsg") == 'ok':
        return f'{title}发送成功......'



bot = Bot(console_qr=-2,cache_path=True)



@bot.register()
def print_others(msg):
    # if '已更新。 详情请点击' not in str(msg):

        articles = msg.articles


        print('msg:' + str(msg),articles)
        if articles:

            if articles is not None:
                    sql = 'select name from weixin where wxcat = 1 '
                    conn1.ping(reconnect=True)
                    cur1.execute(sql)
                    media_list2 = [i[0] for i in cur1.fetchall()]
                    for article in articles:
                        title = article.title
                        links = article.url
                        if 'biz' in links and 'sn=' in links and '橘涞' not in title:
                            link = links.split('&chksm=')[0]

                            int_time, post_time, meida, meida_orig, content, biz, content_p = detail_content(title,
                                link)
                            with open('已采集微信列表.csv','a',encoding='utf8',newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow([meida,int_time])
                            logger.debug((biz, title.strip(), link, meida))
                            if meida in media_list2:

                                result = insert_data(biz, title, content, int_time, meida, '',meida,meida, link, '微信')

                            else:

                                result = insert_data(biz, title, content, int_time, meida, '', meida, meida_orig, link,
                                '微信')
                            if result in ['成功', None]:
                                send_data(title, meida, post_time, link, content[:8])
                                conn2.ping(reconnect=True)
                                sql = """insert into data(biz,title,text,html,link,media,datetime,media_id,type)values(%s,%s,"%s",%s,%s,%s,%s,%s,%s)"""
                                cur2.execute(sql, (biz, title, content_p, content, link, meida, post_time, meida, "微信"))
                                conn2.commit()
                            print(meida,meida_orig,result,1111111111)

        else:
            print('msg:没有阅读号...' + str(msg))
            # send_data('信息','微信',today ,msg)


@logger.catch
def detail_content(title,link):

    all_content = []
    contents_url = link
    # contents_url = '&'.join(update_url)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}

    response = requests.get(contents_url, headers=header).text
    re_times = re.findall(re.compile(r'ct = (.*?);'), str(response))
    re_time = re.search(r'\d+', re_times[0]).group(0)
    Other_time = time.localtime(int(re_time))
    post_time = time.strftime('%Y%m%d %H:%M:%S', Other_time)
    doc = pq(response)
    if len(re_times) == 1:

        # 发布时间

        meida = doc("span.rich_media_meta.rich_media_meta_nickname a").text().strip()
        media_ori = doc("p.original_primary_card_tips span").eq(0).text()
        if media_ori:
            media_ori = re.search('以下文章来源于(.*)', str(media_ori)).group(1)
        else:
            media_ori = meida
        soup_doc = doc('div.rich_media_content').remove("a").text()
        content = re.compile(u'[\U00010000-\U0010ffff]').sub(u'', soup_doc)
        biz = re.search(r'biz=(.*?)&mid', str(link)).group(1)
        content_model = doc('div.rich_media_content').remove("pre")
        all_content.append(title)
        contentes = content_model('p').items()

        for info in contentes:
            all_content.append(''.join(re.findall(re.compile('[\u4E00-\u9FA50-9]+'), str(info.text()))))
            while '' in all_content:
                all_content.remove('')
        if len(all_content) <= 3:
            contentes = content_model('section').items()
            for info in contentes:
                all_content.append(''.join(re.findall(re.compile('[\u4E00-\u9FA50-9]+'), str(info.text()))))
                while '' in all_content:
                    all_content.remove('')
        if len(all_content) <= 3:
            contentes = content_model('div').items()
            for info in contentes:
                all_content.append(''.join(re.findall(re.compile('[\u4E00-\u9FA50-9]+'), str(info.text()))))
                while '' in all_content:
                    all_content.remove('')
    else:
        meida = doc('div.account_nickname strong').text().strip()
        media_ori = meida
        content = doc('div.rich_media_area_primary_inner').text().strip()+meida
        content = ''.join(re.findall(r'[\u4E00-\u9FA50-9]+|。|？|！', content))
        biz = re.search(r'biz=(.*?)&mid', str(link)).group(1)
        all_content = content
    return post_time.split(' ')[0],post_time,meida,media_ori,content,biz,all_content



if __name__ == '__main__':
    # 或者仅仅堵塞线程
    bot.join()
# import csv
#
# import wxpy as wp
# import re
# bot = wp.Bot(cache_path=True)
#
# mps=bot.mps()
# a = [re.search(r'<MP: (.*?)>',str(i)).group(1) for i in mps]
# for i in a:
#     with open('微信实时列表.csv','a',encoding='utf8',newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow([i,])