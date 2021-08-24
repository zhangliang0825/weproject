# -*- coding: utf-8 -*-
import copy
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
import os
from typing import Dict
import time
import execjs
import pymysql
import requests
from scrapy.spiders import CrawlSpider

from ..tools import getLoger
import scrapy
from redis import Redis
from scrapy.utils.project import get_project_settings
from loguru import logger
from urllib import parse

1111
 # 表示当前所处的文件夹上一级文件夹的绝对路径


class ToutiaoSpider(scrapy.Spider):
    new_time = time.time()
    now_day = time.strftime('%Y-%m-%d%H-%M-%S', time.localtime(time.time()))
    name = 'tt_id_'

    allowed_domains = ['toutiao.com']
    # start_urls = ['http://toutiao.com/']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Cookie': 'csrftoken=f0b1ad679f229da355e6c9ac522bb981; ttcid=d3084767ea704fefa6ddac7936408d3333; ttwid=1%7CEQqaQRGYqJHbM6vjddSmseATuLjWIh4Z9_nFPJ-svOk%7C1618548534%7C856d84a0502778e67a6e728a9e1cb2eba340d91e1bc2d4e72acdfcf1f4d6fbf1; s_v_web_id=verify_knqrfnbk_EHxIS7bL_NdHR_4dbn_Bzmw_KYn8e3KQLxgJ; __tasessionId=zt2frug8s1618967482056; csrftoken=f0b1ad679f229da355e6c9ac522bb981; csrftoken=f0b1ad679f229da355e6c9ac522bb981; MONITOR_WEB_ID=3966c7e3-725e-4eb6-b131-274771bed1b6; tt_webid=6951613006950188581',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }, 'DOWNLOAD_TIMEOUT': 15,
        'REDIRECT_ENABLED': False,
        'DOWNLOAD_DELAY': 0.4,
        'CONCURRENT_REQUESTS': 2,



        'DOWNLOADER_MIDDLEWARES': {
            # 'toutiao.middlewares.UserAgentDownloadMiddleware': 500,

            # 'toutiao.middlewares.RandomProxy': 600,
            'ceshi.middlewares.locationproxy':600
        },
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        get_setting = get_project_settings()
        self.cookies = 'csrftoken=f0b1ad679f229da355e6c9ac522bb981; ttcid=d3084767ea704fefa6ddac7936408d3333; ttwid=1%7CEQqaQRGYqJHbM6vjddSmseATuLjWIh4Z9_nFPJ-svOk%7C1618548534%7C856d84a0502778e67a6e728a9e1cb2eba340d91e1bc2d4e72acdfcf1f4d6fbf1; s_v_web_id=verify_knqrfnbk_EHxIS7bL_NdHR_4dbn_Bzmw_KYn8e3KQLxgJ; __tasessionId=yv4zu43gh1618969410644; csrftoken=f0b1ad679f229da355e6c9ac522bb981; MONITOR_WEB_ID=3966c7e3-725e-4eb6-b131-274771bed1b6; csrftoken=f0b1ad679f229da355e6c9ac522bb981; tt_webid=6951613006950188581'


        self.cookies1 = get_project_settings().get("COOKIES_TT_JS")
        self.redis = Redis(host="tz6.zhangyupai.net", password="Lz@12@12@julai", port=6379, db=8)

        self.host = get_setting.get("MYSQL_HOST3")
        self.user = get_setting.get("MYSQL_USER3")
        self.password = get_setting.get("MYSQL_PASSWORD3")
        self.database = get_setting.get("MYSQL_DATABASE4")
        self.mylog = getLoger(self.name + '.log')


    def get_as_cp_signature(self, meida: str,cookie:str, behot_time: int = 0) -> Dict[str, str]:

        params = {
        'category':'profile_all',
        'utm_source':'toutiao',
        'visit_user_token':meida,
        'max_behot_time':behot_time,
        '_signature':'',
                }
        path2 = os.path.abspath('..')
        url = f'https://www.toutiao.com/toutiao/api/pc/feed/?category=profile_all&utm_source=toutiao&visit_user_token={meida}&max_behot_time=0'
        path1 = path2 + r'/ceshi/ceshi/js/_get_as_cp_signature.js'
        sign = os.popen('node {path1} {url} {cookies}'.format(path1 = path1,url='"' + url + '"', cookies='"' + cookie + '"'))
        sigin = sign.read().strip()

        params['visit_user_token'] = meida
        params['_signature'] = sigin
        return params


    def start_requests(self):

        self.ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()  # 创建游标
        sql = 'select num from num_crawl where id = 2'
        self.cursor.execute(sql)
        self.num = self.cursor.fetchone()[0]
        self.end_num = self.num+1
        sql = 'update num_crawl set num = %s where id =2'
        self.cursor.execute(sql, (self.end_num))
        self.db.commit()
        sql = '''SELECT distinct media,link,token,url,is_jj FROM media WHERE post_type IN (1) AND link <> "" and token is not NULL and id between 6000 AND 12000 and TYPE IS NULL'''
        self.cursor.execute(sql)
        all_data_list = self.cursor.fetchall()
        for meida, media_id, token,start_num,is_jj in all_data_list:

            first_params = self.get_as_cp_signature(token,self.cookies)
            first_params['visit_user_token'] = token
            indexurls = 'https://www.toutiao.com/api/pc/feed/?'
            index_url = indexurls + parse.urlencode(first_params)
            if start_num == None:
                start_num = 0

            if int(self.num) - int(start_num)>1:
                print(int(self.num) - int(start_num),int(self.num),start_num,'数字通过')
         
                meta = {'media': media_id, 'token': token, 'dont_redirect': True,
                     'handle_httpstatus_list': [301],'is_jj':is_jj}

                yield scrapy.Request(index_url, callback=self.parse,meta=copy.deepcopy(meta),
                                dont_filter=True)


    def parse(self, response):

        i = 0

        yesterday_format = datetime.today() + timedelta(-1)
        yesterday = yesterday_format.strftime('%Y%m%d')
        r_data = json.loads(response.text).get("data")

        media = response.meta['media']

        if r_data:
            self.mylog.info((media, '数据正常'))
            sql = 'update media set url = %s where link =%s'
            self.cursor.execute(sql, (self.num,media))
            self.db.commit()
            for item in r_data:

                if 'group_cell' in item:
                    id_s = item.get("base_cell")

                    if id_s:

                        created_time = id_s.get("log_pb")

                        if 'create_time' in created_time:
                            created_time = created_time.get("create_time")
                            Other_time = time.localtime(int(created_time))
                            post_time_s = time.strftime('%Y%m%d', Other_time)
                            if post_time_s>= yesterday:
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
                                # if 'answer' in answer:
                                #     answer_time = answer.get('answer').get('create_time')
                                Other_time_answer = time.localtime(int(answer_time))
                                created_time = time.strftime('%Y%m%d', Other_time_answer)
                            else:
                                created_time = raw_data.get("comment_base").get("create_time")

                            if '内' in created_time or created_time>=yesterday:
                                id_ = id_s.get("log_pb").get("logpb_group_id")
                            else:
                                id_ = None
                else:
                    i += 1
                    behot_time = item.get("behot_time")

                    if i == 2 and any(i in behot_time for i in ['月前', '年前']):
                        sql = 'update media set post_type = %s where link =%s'
                        self.cursor.execute(sql, (2, media.strip()))
                        self.db.commit()

                    if '前' in behot_time:
                        continue
                    id_ = item.get("item_id")

                if id_:
                    index_url = 'https://toutiao.com/i{}'.format(id_)
                    ex = self.redis.sadd('crawledtt_url', index_url)
                    if ex == 1:
                        if 'iNone' not in index_url:

                            self.redis.lpush('TTurl:start_urls', index_url)
                            self.mylog.info((media, index_url, '数据进库....'))




        else:
            sql = 'update media set post_type = %s where link =%s'
            self.cursor.execute(sql, (3, media.strip()))
            self.db.commit()
            print(media,'没有数据的key1')