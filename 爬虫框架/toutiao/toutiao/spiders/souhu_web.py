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


class SouhuSpider(scrapy.Spider):


    name = 'souhu_web'
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


    def start_requests(self):
        urls = ['http://v2.sohu.com/public-api/feed?scene=TAG&sceneId=66047&page={}&size=20'.format(i) for i in
                range(1, 30)]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse, cookies=self.cookies, dont_filter=True)


    def parse(self, response):
       json_data = json.loads(response.text)
       if json_data != []:
           for item in json_data:
               authorName = item.get("authorName")
              
               title = item.get("title")
               publicTime = str(item.get("publicTime"))[:-3]
               formattime = time.localtime(int(publicTime))
               post_time = time.strftime('%Y%m%d', formattime)
               text_id = item.get("id")
               authorId = item.get("authorId")
               index_url = 'https://www.sohu.com/a/{}_{}'.format(text_id, authorId)
               if authorName in self.all_data:
                   continue
               self.redis.lpush('TTurl:start_urls', index_url)

               sql = '''insert into souhu(names,media)  values (%s,%s)'''
               self.cursor.execute(sql, (authorName, authorId))
               self.db.commit()
               print(authorId,text_id,post_time,title,authorName,index_url)

