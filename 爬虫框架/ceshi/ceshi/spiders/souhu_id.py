import copy
import hashlib
import re
from datetime import datetime, timedelta

import pymysql
import base64
import json
import random
import sys
import time
from urllib.parse import urlencode
import pymysql
import requests
import scrapy
from redis import Redis
from scrapy.utils.project import get_project_settings
from ..tools import getLoger


class SouhuSpider(scrapy.Spider):


    name = 'souhu_id'
    allowed_domains = ['www.sohu.com/']

    custom_settings = {
        'DOWNLOAD_DELAY':0.2,
        'CONCURRENT_REQUESTS' : 26
    }

    def __init__(self, **kwargs):
        self.headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

        }
        self.redis = Redis(host="tz6.zhangyupai.net", password="Lz@12@12@julai", port=6379, db=8)
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
        self.mylog = getLoger(self.name + '.log')


    def md5(self,souhu_id,page,id_):
        md5 = hashlib.md5()

        rs = souhu_id + str(page) + id_
        md5.update(rs.encode('utf-8'))
        newmd5 = md5.hexdigest()
        return newmd5

    def start_requests(self):
        for name,name_id in self.all_data:
            id_code_url = f'https://v2.sohu.com/author-page-api/getEncryptJs?callback=setSecret&authorId={name_id}'
            response = requests.get(id_code_url)
            id_code = re.search(r"\+'(.*?)'\);", response.text).group(1)
            for page in range(1,3):
                time.sleep(0.3)
                newmd5 = self.md5(name_id,page,id_code)
                url = f'http://v2.sohu.com/author-page-api/author-articles/pc/{name_id}?pNo={page}&secretStr={newmd5}'
                yield scrapy.Request(url,callback=self.parse,dont_filter=True,meta=copy.deepcopy({'name':name}))

    def parse(self, response):
        name = response.meta['name']
        status_code = response.status

        if status_code == 404:
            sql = 'delete from souhu where names = %s'
            self.cursor.execute(sql,name)
            self.db.commit()
            print('已删除...',name,sql)
        else:
            yesterday_format = datetime.today() + timedelta(-1)
            yesterday = yesterday_format.strftime('%Y%m%d')
            json_data = json.loads(response.text)
            for info in json_data.get('data').get('pcArticleVOS'):
                created =str(info.get('publicTime'))[:-3]
                created_time = time.localtime(int(created))
                str_date = time.strftime('%Y%m%d',created_time)
                if str_date>= yesterday:

                    link = 'https://'+info.get('link')
                    self.mylog.info((name, link))
                    ex = self.redis.sadd('crawledsh_url', link)
                    if ex == 1:
                        self.mylog.info((name,link))
                        self.redis.lpush('SHurl:start_urls', link)
                        print(name,link,'已插入数据..')








