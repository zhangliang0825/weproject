# -*- coding: utf-8 -*-
import base64
import json
import random
import sys
import time
from urllib.parse import urlencode
import pymysql

import scrapy

from redis import Redis
from scrapy.utils.project import get_project_settings
from loguru import logger
import asyncio
CONCURRENCY = 6
semaphore = asyncio.Semaphore(CONCURRENCY)


logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")



class SouhuSpider(scrapy.Spider):


    name = 'souhu'
    allowed_domains = ['www.sohu.com/']
    def __init__(self, **kwargs):
        self.headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

        }
        self.redis = Redis(host="tz6.zhangyupai.net", password="Lz@12@12@12@", port=6379, db=8)
        get_setting = get_project_settings()
        self.host = get_setting.get("MYSQL_HOST3")
        self.user = get_setting.get("MYSQL_USER3")
        self.password = get_setting.get("MYSQL_PASSWORD3")
        self.database = get_setting.get("MYSQL_DATABASE4")
        self.cookies = get_project_settings().get("COOKIES_TT_WEB3")
        self.db = pymysql.connect(self.host, self.user,
            self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()
        sql = '''select names from souhu'''
        self.cursor.execute(sql)
        self.all_data = [i[0] for i in self.cursor.fetchall()]
        self.word_data = ['中信信诚','华夏幸福','包商银行','博时基金',"基金", '交银基金', '交银施罗德','长信基金', '嘉实基金', '国泰元鑫', '国泰基金', '富国基金', '南方基金', '招商基金', '银华基金', '新华基金', '平安基金',
                          '兴全基金', '兴证全球','东证资管','东方红基金'
                          '中欧基金', '鹏华基金', '鹏华基金', '中邮基金', '华夏基金', '易方达', '华安基金', '华商基金', '民生加银', '富安达基金', '中信保诚','东证资管'
                          '国海富兰克林']

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
    
        # print(response.request.headers)
        data_json = json.loads(response.text)
        all_data = data_json.get('data').get('news')
        for info in all_data:
            authorName = info.get('authorName')
            authorId = info.get('authorId')
            if authorName in self.all_data:
                continue
            title = info.get('title')
            url = info.get('url').replace('http','https')
            self.redis.lpush('TTurl:start_urls', url)
            postTime = str(info.get('postTime'))[:-3]
            postTime = time.localtime(int(postTime))
            other_time = time.strftime('%Y%m%d',postTime)
            print(url)

            sql = '''insert into souhu(names,media)  values (%s,%s)'''
            self.cursor.execute(sql,(authorName,authorId))
            self.db.commit()

            # yield scrapy.Request(url,callback=self.detail_parse,dont_filter=True,cookies = self.cookies,
            #     meta={'title':title,'other_time':other_time,'authorName':authorName}
            #    )




