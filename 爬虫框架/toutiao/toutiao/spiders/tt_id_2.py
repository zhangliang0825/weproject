# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path
import os
from typing import Dict
import time
import execjs
import pymysql
import requests
from ..tools import getLoger
import scrapy
from redis import Redis
from scrapy.utils.project import get_project_settings
from loguru import logger
from urllib import parse

# toutiao_dir = Path(__file__).absolute().parent
path2 = os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹的绝对路径


class TtIdSpider(scrapy.Spider):
    new_time = time.time()
    now_day = time.strftime('%Y-%m-%d%H-%M-%S', time.localtime(time.time()))
    name = 'tt_id_2'

    allowed_domains = ['toutiao.com']
    # start_urls = ['http://toutiao.com/']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'Cookie': '__utmz=24953151.1592959631.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PIXIEL_RATIO=1.5; sso_auth_status=ff666bef2638d04593de6c1619a008f0; sso_uid_tt=3aab2c0d7e6b017b0ea25f2dc09e7ec4; sso_uid_tt_ss=3aab2c0d7e6b017b0ea25f2dc09e7ec4; toutiao_sso_user=6b202cdd3c7266fdee4250dd777c6c58; toutiao_sso_user_ss=6b202cdd3c7266fdee4250dd777c6c58; passport_auth_status=374941f129ff88fee478dbf9632801be%2Cd6cbe685fe989c938d5cbfd3c56dc9ea; sid_guard=6d59bafe68b1d4985bbafd8acc5f815a%7C1594191164%7C5184000%7CSun%2C+06-Sep-2020+06%3A52%3A44+GMT; uid_tt=36eb4fca4ae8694c71028232f426bf92; uid_tt_ss=36eb4fca4ae8694c71028232f426bf92; sid_tt=6d59bafe68b1d4985bbafd8acc5f815a; sessionid=6d59bafe68b1d4985bbafd8acc5f815a; sessionid_ss=6d59bafe68b1d4985bbafd8acc5f815a; tt_webid=6846998871970448904; __utma=24953151.710770063.1592959631.1592959631.1594278577.2; SLARDAR_WEB_ID=6846998871970448904; RT="z=1&dm=toutiao.com&si=fnn5vftq4q7&ss=kcfz3q4v&sl=1&tt=0&obo=1&ld=3bnp20&r=bbe4ce7ddc46c6df117239442a065abc&ul=3bnp25&hd=3bnp2l"; WIN_WH=1280_578; tt_webid=6843736986450331143',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        }, 'DOWNLOAD_TIMEOUT': 15,
        'REDIRECT_ENABLED': False,
        'DOWNLOADER_MIDDLEWARES': {
            # 'toutiao.middlewares.UserAgentDownloadMiddleware': 500,

            # 'toutiao.middlewares.RandomProxy': 600,
            'toutiao.middlewares.locationproxy':600
        },
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        get_setting = get_project_settings()

        self.cookies = get_setting.get("COOKIES_TT")

        self.redis = Redis(host="tz6.zhangyupai.net", password="Lz@12@12@12@", port=6379, db=0)

        self.host = get_setting.get("MYSQL_HOST3")
        self.user = get_setting.get("MYSQL_USER3")
        self.password = get_setting.get("MYSQL_PASSWORD3")
        self.database = get_setting.get("MYSQL_DATABASE4")
        self.mylog = getLoger(self.name + '.log')


    def start_requests(self):

        self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()  # 创建游标
        sql = '''SELECT media,link,token FROM media WHERE post_type IN (1) AND link <> "" and token is not NULL and id >=8000 and TYPE IS NULL'''
        self.cursor.execute(sql)
        all_data_list = self.cursor.fetchall()
        for meida, media_id, token in all_data_list:
            print(meida, media_id, token,)

            first_params = self.get_as_cp_signature(token,self.cookies)
            first_params['visit_user_token'] = token
            index_url = 'https://www.toutiao.com/api/pc/feed/?'
            index_url = index_url + parse.urlencode(first_params)
            print(index_url)
            yield scrapy.Request(index_url, callback=self.parse, meta={'media': media_id, 'token': token},
                dont_filter=True)

    def get_as_cp_signature(self, meida: str,cookie:str, behot_time: int = 0) -> Dict[str, str]:

        params = {
'category':'profile_all',
'utm_source':'toutiao',
'visit_user_token':behot_time,
'max_behot_time':'0',
'_signature':'',
        }

        url = f'https://www.toutiao.com/toutiao/api/pc/feed/?category=profile_all&utm_source=toutiao&visit_user_token={meida}&max_behot_time=0'
        path1 = path2 + r'/toutiao/toutiao/js/sigin.js'
        sign = os.popen('node {path1} {url} {cookies}'.format(path1 = path1,url='"' + url + '"', cookies='"' + cookie + '"'))
        sigin = sign.read().strip()
        params['visit_user_token'] = meida
        params['_signature'] = sigin
        return params

    def parse(self, response):
        i = 0

        r_data = json.loads(response.text).get("data")

        media = response.meta['media']

        token = response.meta['token']

        sql = 'update media set token = %s where link =%s'

        self.cursor.execute(sql, (token, media))
        self.db.commit()
        if r_data:
            for item in r_data:
                if 'group_cell' in item:
                    id_s = item.get("stream_cell")
                    if id_s:
                        id_ = json.loads(id_s.get("raw_data")).get("item_id")
                    else:
                        concern_talk_cell = item.get("concern_talk_cell")
                        if concern_talk_cell:
                            id_ = concern_talk_cell.get("id")
                else:
                    i += 1
                    behot_time = item.get("behot_time")
                    if i == 2 and any(i in behot_time for i in ['月前', '年前']):
                        sql = 'update media set post_type = %s where media =%s'
                        self.cursor.execute(sql, (2, media.strip()))
                        self.db.commit()
                        print(behot_time, media,22222222222222222222222,'推送的时间太长了.....')
                    id_ = item.get("item_id")
                index_url = 'https://www.toutiao.com/i{}/'.format(id_)
                if 'iNone' not in index_url:
                    self.redis.lpush('TTurl:start_urls', index_url)

                    self.mylog.info((media,index_url))
                    print(index_url)
        else:
            print(media, 11111111111111111)
        #
        # data_json = json.loads(response.text)
        # media = response.meta.get("media")
        #
        #
        #
        # data_list = data_json.get("data")
        # if data_list:
        #     keyword = [i.get("id") for i in data_list if i.get("name") ==media.strip()]
        #     if keyword:
        #         sql = 'update media set link = %s where media =%s'
        #         self.cursor.execute(sql, (keyword[0], media.strip()))
        #         self.db.commit()
        #         print(keyword,media)
        #     else:
        #         sql = 'update media set link = %s where media =%s'
        #         self.cursor.execute(sql, ('', media.strip()))
        #         self.db.commit()
        #         print(keyword, media)
        # else:
        #     sql = 'update media set link = %s where media =%s'
        #     self.cursor.execute(sql, ('', media.strip()))
        #     self.db.commit()
        #     print( media)

        '''更新meida的id代码'''
