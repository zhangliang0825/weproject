import base64

import requests
import json
import re

from bs4 import BeautifulSoup
from pyquery import PyQuery as qp
import random
import demjson
import redis

pool = redis.ConnectionPool(host='tz6.zhangyupai.net', port=6379, db=1, password='Lz@12@12@julai')
r = redis.Redis(connection_pool=pool)
import pymysql
import time
import multiprocessing
import datetime

print(datetime.date.today())
today = datetime.date.today().weekday()
print(today)

now = time.time()

midnight = now - (now % 86400) + time.timezone

if today == 6:
    prenight = midnight - 86400 * 3
else:
    prenight = midnight - 86400 * 3
end_time = prenight
timeArray = time.localtime(end_time)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime, 111111111111)

dbhost = '120.26.211.213'
dbuser = 'julai01'
passwd = 'Zycj@2020688'
dbname = 'news_caiji'
conn = pymysql.connect(dbhost, dbuser, passwd, dbname, charset='utf8')
cur = conn.cursor()

dbname2 = 'weixin'
conn3 = pymysql.connect(dbhost, dbuser, passwd, dbname2, charset='utf8')
cur3 = conn3.cursor()


def get_date(query):
    print(otherStyleTime)
    global token, data, Now_Time, id_data
    if query == '富国基金':
        query = 'fuguo1999'
    elif query == "嘉实基金":
        query = "js-fund"
    elif query == '南方基金微视界':
        query = 'NFJJ4008898899'
    elif query == '新华基金':
        query = 'gh_aa9f52c1bb3a'
    elif query == '平安基金微视界':
        query = 'pinganfund'
    elif query == '平安基金':
        query = 'pingandahua'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}
    pool = redis.ConnectionPool(host='tz6.zhangyupai.net', port=6379, db=1, password='Lz@12@12@julai')
    r = redis.Redis(connection_pool=pool)
    key = r.randomkey()
    cookie = demjson.decode(r.get(key).decode())
    url = 'https://mp.weixin.qq.com/'
    print(cookie)
    try:
        resp = requests.get(url, headers=header, cookies=cookie).url
        token = re.findall(r'token=(\d+)', str(resp))[0]
        data = {'action': 'search_biz',
                'token': token,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': '1',
                'random': random.random(),
                'query': query,
                'begin': '0',
                'count': '5'}

        search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
        time.sleep(1)
        search_resp = requests.get(search_url, headers=header, cookies=cookie, params=data)
        id_data = search_resp.json().get('list')[0].get('fakeid')
        wx_id = search_resp.json().get('list')[0].get('alias')
        post_data = {'token': token,
                     'lang': 'zh_CN',
                     'f': 'json',
                     'ajax': '1',
                     'random': random.random(),
                     'action': 'list_ex',
                     'begin': '0',
                     'count': '5',
                     'query': '',
                     'fakeid': id_data,
                     'type': '9', }
        content_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
        time.sleep(1)
        contents = requests.get(content_url, headers=header, cookies=cookie, params=post_data).text
        all_info = json.loads(contents)
        app_msg = all_info.get('app_msg_list')
    except Exception as e:
        if e:
            print(key)
            r.delete(key, )
    try:
        for info, items in enumerate(app_msg):
            title = items.get('title')
            link = items.get('link')
            update_url = link.split('&')[:-1]
            contents_url = '&'.join(update_url)  # 截取过后的网址
            times = items.get('update_time')  # 原有的获取时间
            content_time = items.get('update_time')  # 原有的获取时间
            times_tuple = time.localtime(times)
            post_time = time.strftime('%Y%m%d', times_tuple)

            Now_time = int(time.time())
            if end_time <= content_time <= Now_time:
                top = re.findall(re.compile(r'idx=(\d+)&'), str(contents_url))[0]
                html = requests.get(link, cookies=cookie).text
                doc = qp(html)
                original = doc('div .rich_media_meta_list #copyright_logo').text()
                # author = re.findall(re.compile(r'作者 (.*)'),doc('div .rich_media_meta_list p.rich_media_meta_primary').text())[0]
                contents = doc('div.rich_media_content').remove('a').text()

                content = re.compile(u'[\U00010000-\U0010ffff]').sub(u'', contents)
                soup = BeautifulSoup(html, 'lxml')

                page_content = str(soup.select('div#page-content')[0]).replace('data-src="',
                    'src="http://img01.store.sogou.com/net/a/04/link?appid=100520029&url=').replace('publish_time">',
                    'publish_time">{}'.format(post_time))
                media = doc("span.rich_media_meta.rich_media_meta_nickname a").text()
                author = doc('div .rich_media_meta_list p.rich_media_meta_primary')
                if author:
                    author = re.findall(re.compile(r'作者 (.*)'), author.text())[0]
                else:
                    author = ''
                if query == 'fuguo1999':
                    query = '富国基金'
                elif query == "js-fund":
                    query = "嘉实基金"
                elif query == 'NFJJ4008898899':
                    query = '南方基金'
                elif query == 'gh_aa9f52c1bb3a':
                    query = '新华基金'
                elif query == 'pinganfund':
                    query = '	平安基金微视界'
                elif query == 'pingandahua':
                    query = '平安基金'
                if top != '1':
                    top = 0

                insert_data(id_data, title, content, int(post_time), original, author, media, contents_url, '微信',
                    page_content)

                print(title, times, original, author, query,media, contents_url, top)
    except Exception as e:
        print(e)


def insert_jinxian(post_id, content):
    try:
        sql = 'insert into weixin_jj(post_id,content) values (%s,%s)'
        cur3.execute(sql, (post_id, content))
        conn3.commit()
        return 1
    except Exception as e:
        if e:
            return -1


def insert_data(id_data, title, content, times, original, author, query, contents_url, spider, img_content):
    global data

    data = {
        'title': title,
        'str_date': times,
        'digest': '',
        'media_orig': query,
        'content': content,
        'bizname': query,
        'content_url': contents_url,
        'biz': id_data,
        'readNum': '',
        'is_orig': original,
        'reporter': author,
        'spider': spider,
    }

    for i in range(1, 10):
        print(i)
        try:
            insert_url = ' http://tz4.zhangyupai.net:81/mobile/import_wxpost.php'
            resp = requests.post(insert_url, data=data, timeout=7).text
            print(resp)
            if '1' in resp:
                print(f'数据第{i}进库成功...')
                return '数据进库成功'

                # post_id = re.search(r'post_id=(.*)',str(resp)).group(1).strip()
                # reslut = insert_jinxian(post_id,img_content)
                # print(reslut,888888888888888)

        except Exception as e:
            print(e)


# def name_list():
#     dbhost = '120.26.211.213'
#     dbuser = 'huanghai'
#     passwd = 'huanghai_password'
#     dbname = 'news_caiji'
#     conn = pymysql.connect(dbhost, dbuser, passwd, dbname, charset='utf8')
#     cur = conn.cursor()
#
#     sql = '''SELECT DISTINCT id,NAME FROM weixin WHERE collect=1 and wxcat IN (1)
#     '''
#     cur.execute(sql)
#     rs = list(cur.fetchall())
#     print(rs)
#     return rs


if __name__ == '__main__':


    with open('微信实时列表.csv', 'r', encoding='utf8') as p:
        # all_media_all_list = set([i.strip() for i in f.readlines()])
        all_media_all_list = [i.strip() for i in p.readlines() if i.strip()!='']
        all_media_all_set = sorted(list(set(all_media_all_list)),key=all_media_all_list.index)
        p.close()
    with open('已采集微信列表.csv', 'r', encoding='utf8') as f:
        # all_shishi_crawled_list = set(i.strip() for i in f.readlines())
        all_shishi_crawled_list = list(set([i.split(',')[0].strip() for i in f.readlines()]))

    tap_media = [i for i in all_media_all_set if i not in all_shishi_crawled_list ]

    with open('已采集微信列表.csv', 'r+', encoding='utf8') as f:
        f.truncate(0)


    for item in tap_media:
        time.sleep(1)
        print(item)
        get_date(item)



