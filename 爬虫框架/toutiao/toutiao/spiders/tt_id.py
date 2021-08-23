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
from scrapy import Request

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
    name = 'tt_id'

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
            # 'toutiao.middlewares.locationproxy':600
        },
    }
    base_url = 'https://www.baidu.com/s?wd='
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        get_setting = get_project_settings()
        self.cookies = get_setting.get("COOKIES_TT")
        self.redis  = Redis.from_url(get_setting.get("REDIS_URL"))
        self.db_config = get_setting.get("DB_CONFIG")
        self.mylog = getLoger(self.name + '.log')

    def start_requests(self):
        for i in range(10):
            url = self.base_url + str(i)
            yield Request(url, callback=self.parse)

        # Here contains 10 duplicated Requests
        for i in range(100):
            url = self.base_url + str(i)
            yield Request(url, callback=self.parse)

    def parse(self, response):
        self.logger.debug('Response of ' + response.url)
