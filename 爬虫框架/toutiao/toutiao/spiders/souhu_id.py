import hashlib



import pymysql
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


    name = 'souhu_id'
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
        sql = '''select distinct names,media from souhu where ty is null'''
        self.cursor.execute(sql)
        self.all_data = [i for i in self.cursor.fetchall()]

    def md5(self,souhu_id):
        md5 = hashlib.md5()
        rs = souhu_id + '1' + 'ECqEvgdFOCt9jvMC1b9cad2'
        md5.update(rs.encode('utf-8'))
        newmd5 = md5.hexdigest()
        return newmd5

    def start_requests(self):
        for name,name_id in self.all_data:
            newmd5 = self.md5(name_id)
            url = f'http://v2.sohu.com/author-page-api/author-articles/pc/{name_id}?pNo=1&secretStr={newmd5}'
            yield scrapy.Request(url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        json_data = json.loads(response.text)
        for info in json_data.get('data').get('pcArticleVOS'):
            link = 'https://'+info.get('link')
            self.redis.lpush('TTurl:start_urls', link)
            print(link)




