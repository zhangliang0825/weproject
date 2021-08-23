import re
import time

import pymysql
import scrapy
from redis import Redis
from scrapy.utils.project import get_project_settings
from ..tools import getLoger
import datetime


class DataInsertSpider(scrapy.Spider):
    name = 'insert_1_data'
    allowed_domains = ['zhangyupai.net']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'

        },
        'CONCURRENT_REQUESTS' : 20,
        'DOWNLOAD_DELAY': 0.3,
        'DOWNLOAD_TIMEOUT': 10,
       'REDIS_URL' : 'redis://root:Lz@12@12@julai@tz6.zhangyupai.net:6379/9'

    #     'SCHEDULER' : '',
    #
    # 'DUPEFILTER_CLASS' :''

    }

    # start_urls = ['http://zhangyupai.net/']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        get_setting = get_project_settings()


        self.cookies = get_setting.get("COOKIES_TT")

        self.redis = Redis(host="tz6.zhangyupai.net", password="Lz@12@12@12@", port=6379, db=9)
        print(self.redis)
        self.host = get_setting.get("MYSQL_HOST2")
        self.user = get_setting.get("MYSQL_USER2")
        self.password = get_setting.get("MYSQL_PASSWORD2")
        self.database = get_setting.get("MYSQL_DATABASE3")
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()
        # self.post_url = 'http://tz4.zhangyupai.net:81/mobile/import_ttnews1.php'
        self.mylog = getLoger(self.name + '.log')

    def start_requests(self):
        start_num = self.redis.get('insert_data_id_zimeiti').decode('utf8')

        sql = 'select id,title,text,html,link,media,datetime,media_id,type from data where id>%s and type not in ("微博","微信")'
        self.cursor.execute(sql, start_num)
        all_data_list = self.cursor.fetchall()
        if all_data_list:
            for id_, title, text, html, link, media, datetime_, media_id, type_ in all_data_list:
                if '-' in datetime_:
                    datetime_ = ''.join(re.split(r'-|\s+',datetime_)[:3])

                else:
                    datetime_ = datetime_

                souhu_url = 'http://tz4.zhangyupai.net:81/mobile/import_mynews1.php'
                tt_url = 'http://tz4.zhangyupai.net:81/mobile/import_ttnews1.php'
                wx_url =  'http://tz4.zhangyupai.net:81/mobile/import_wxpost.php'
                if 'com/i' in  link:
                    type_num = 6
                    url = tt_url
                elif 'com/w/' in link:
                    type_num = 17
                    url = tt_url
                elif type_ == '搜狐':
                    type_num = 14
                    url = souhu_url
                elif type_ == '搜狗':
                    type_num = 3
                    url = wx_url
                if type_num ==3:
                    data = {'title': title, 'content': html, 'post_type': str(type_num), 'summary': html[:60], 'media_orig': media_id,
                            'reporter': '', 'content_url': link, 'str_date': datetime_, 'username':media, 'is_orig': '1',
                            'meta_info': '', 'spider': type_, 'bizname': media,
                            'biz': '', }
                else:
                    data = {'title': title, 'content': html, 'post_type': str(type_num), 'summary': html[:60], 'media_orig': media,
                            'reporter': '', 'content_url': link, 'str_date': datetime_, 'username':type_, 'is_orig': '1',
                            'meta_info': '', 'spider': type_, 'bizname': '',
                            'biz': '', }

                self.mylog.info((type_,link))
                yield scrapy.FormRequest(url, callback=self.parse, formdata=data, dont_filter=True, meta={
                    'id_': id_
                })

    def parse(self, response):
        id_ = response.meta['id_']

        self.redis.set('insert_data_id_zimeiti', id_)
        self.mylog.info(response.text)
        print(response.text, )

