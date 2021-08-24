# -*- coding: utf-8 -*-
import base64
from datetime import datetime,timedelta
import json
import random
import sys
import time
from urllib.parse import urlencode
import pymysql
from ..tools import getLoger
import scrapy

from redis import Redis
from scrapy.utils.project import get_project_settings
from loguru import logger
import asyncio



class SouhuSpider(scrapy.Spider):


    name = 'souhu'
    allowed_domains = ['www.sohu.com/']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'ceshi.middlewares.GetFailedrequsts': 543
        },
        'DOWNLOAD_DELAY':0.5
    }

    def __init__(self, **kwargs):

        self.redis = Redis(host="tz6.zhangyupai.net", password="Lz@12@12@julai", port=6379, db=8)
        get_setting = get_project_settings()
        self.host = get_setting.get("MYSQL_HOST3")
        self.user = get_setting.get("MYSQL_USER3")
        self.password = get_setting.get("MYSQL_PASSWORD3")
        self.database = get_setting.get("MYSQL_DATABASE4")
        self.db = pymysql.connect(self.host, self.user,
            self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()
        sql = '''select names from souhu'''
        self.cursor.execute(sql)
        self.all_data = [i[0] for i in self.cursor.fetchall()]

        sql = '''SELECT DISTINCT NAMES,media FROM souhu WHERE ty =1'''
        self.cursor.execute(sql)
        self.all_data_exclude = [i[0] for i in self.cursor.fetchall()]


        sql = 'select word from words'
        self.cursor.execute(sql)
        sql = 'select word from words where del_flag = 0 ORDER BY choose_flag ASC'
        self.cursor.execute(sql)
        self.word_data = set([i[0].replace("+", " ") for i in self.cursor.fetchall()])
        self.mylog = getLoger(self.name + '.log')


    def get_url(self,s, num=None):
        s = s.encode()
        st = base64.b64encode(s)[:4].decode('utf8')
        ip_ = '009'
        free = f'{199 + 1}'
        if len(st) == 4:
            st = st
        else:
            st = list(st)
            st = ''.join(st.insert(0, '0'))

        timestamp = str(int(time.time() * 1000))[:10]
        QueryId = timestamp + ip_ + st + free

        x = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        res = [x] * 7

        pvId = str(int(time.time() * 1000)) + ''.join(list(map(lambda x: x[int(random.random() * len(x))], res)))

        data = {
            'keyword': s,
            'terminalType': 'pc',
            'ip': '101.88.243.9',
            'city': '上海市',
            'spm-pre': 'smpc.sub-channel.0.0.1609230970237870JFlg',
            'SUV': '20112615431695IO',
            'from': num,
            'size': '10',
            'searchType': 'news',
            'queryType': 'outside',
            'queryId': QueryId,
            'pvId': pvId,
            'refer': '',
            'size': '10',
            'maxL': '15',
            'spm': '',
            '_': str(int(time.time() * 1000)),
        }

        data = urlencode(data)
        url = 'https://search.sohu.com/search/meta?' + data
        return url

    def start_requests(self):
        

        for word in self.word_data:
            for i in range(1,11):
                page = i*10
                url = self.get_url(word,page)
           
                yield scrapy.Request(url,callback=self.parse,dont_filter=True)


    def parse(self, response):
        yesterday = datetime.today() + timedelta(-1)
        yesterday_str = yesterday.strftime('%Y%m%d')
        # print(response.request.headers)
        data_json = json.loads(response.text)
        all_data = data_json.get('data').get('news')

        for info in all_data:
            authorName = info.get('authorName')
            authorId = info.get('authorId')
            print(authorName)

            postTime = str(info.get('postTime'))[:-3]
            postTime = time.localtime(int(postTime))
            other_time = time.strftime('%Y%m%d',postTime)
            
            if other_time>=yesterday_str and authorName not in self.all_data_exclude:
                url = info.get('url').replace('http', 'https')
                ex = self.redis.sadd('crawledsh_url', url)
                print(url,ex)
                if ex ==1:
                    self.redis.lpush('SHurl:start_urls', url)
                    self.mylog.info((url,authorName,other_time))
                    print(url,authorName,other_time)


            if authorName in self.all_data:
                continue
            sql = '''insert into souhu(names,media)  values (%s,%s)'''
            self.cursor.execute(sql,(authorName,authorId))
            self.db.commit()




