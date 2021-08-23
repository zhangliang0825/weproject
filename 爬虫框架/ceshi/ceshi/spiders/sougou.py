# -*- coding: utf-8 -*-
import csv
from datetime import datetime,timedelta,date
import re
from ..tools import getLoger
import time
import os
import pymysql
import requests
import scrapy
from redis import Redis
from scrapy.utils.project import get_project_settings
from loguru import logger
from ..items import CeshiItem

class SougouSpider(scrapy.Spider):

    name = 'sougou'
    allowed_domains = ['weixin.sogou.com']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'Cookie': '__utmz=24953151.1592959631.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PIXIEL_RATIO=1.5; sso_auth_status=ff666bef2638d04593de6c1619a008f0; sso_uid_tt=3aab2c0d7e6b017b0ea25f2dc09e7ec4; sso_uid_tt_ss=3aab2c0d7e6b017b0ea25f2dc09e7ec4; toutiao_sso_user=6b202cdd3c7266fdee4250dd777c6c58; toutiao_sso_user_ss=6b202cdd3c7266fdee4250dd777c6c58; passport_auth_status=374941f129ff88fee478dbf9632801be%2Cd6cbe685fe989c938d5cbfd3c56dc9ea; sid_guard=6d59bafe68b1d4985bbafd8acc5f815a%7C1594191164%7C5184000%7CSun%2C+06-Sep-2020+06%3A52%3A44+GMT; uid_tt=36eb4fca4ae8694c71028232f426bf92; uid_tt_ss=36eb4fca4ae8694c71028232f426bf92; sid_tt=6d59bafe68b1d4985bbafd8acc5f815a; sessionid=6d59bafe68b1d4985bbafd8acc5f815a; sessionid_ss=6d59bafe68b1d4985bbafd8acc5f815a; tt_webid=6846998871970448904; __utma=24953151.710770063.1592959631.1592959631.1594278577.2; SLARDAR_WEB_ID=6846998871970448904; RT="z=1&dm=toutiao.com&si=fnn5vftq4q7&ss=kcfz3q4v&sl=1&tt=0&obo=1&ld=3bnp20&r=bbe4ce7ddc46c6df117239442a065abc&ul=3bnp25&hd=3bnp2l"; WIN_WH=1280_578; tt_webid=6843736986450331143',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }, 'DOWNLOAD_DELAY':1,
        'CONCURRENT_REQUESTS':2,
        'DOWNLOADER_MIDDLEWARES':{
            # 'toutiao.middlewares.RandomProxy':501
            'ceshi.middlewares.locationproxy': 600
        },
        'ITEM_PIPELINES' :{

        'ceshi.pipelines.CeshiPipeline': 301,
    }


    }

    def __init__(self, **kwargs):

        today = date.today()
        oneday = timedelta(days=1)
        yesterday = str(today - oneday)
        get_setting = get_project_settings()
        self.host = get_setting.get("MYSQL_HOST3")
        self.user = get_setting.get("MYSQL_USER3")
        self.password = get_setting.get("MYSQL_PASSWORD3")
        self.database4 = get_setting.get("MYSQL_DATABASE4")
        self.database = get_setting.get("MYSQL_DATABASE5")
        self.db = pymysql.connect(self.host, self.user,
        self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()
        #
        # self.host_jj = get_setting.get("MYSQL_HOST")
        # self.user_jj = get_setting.get("MYSQL_USER")
        # self.password_jj = get_setting.get("MYSQL_PASSWORD")
        # self.database_jj = get_setting.get("MYSQL_DATABASE")

        # self.db_jj = pymysql.connect(self.host_jj, self.user_jj,
        #     self.password_jj, self.database_jj, charset='utf8')
        # self.cursor_jj = self.db_jj.cursor()
        # self.sql1 = f'''select distinct b.title,a.media_channel from hisinfo_cx a inner join cx0308 b on a.`post_id` = b.`id` where a.post_type = 3 and a.str_date >= {yesterday.replace('-','')}'''
        # self.cursor_jj.execute(self.sql1)
        # self.data_list_crawler = [[''.join(re.findall(u'[\u4e00-\u9fa5]', title)), media] for title, media in
        #                           self.cursor_jj.fetchall()]
        # print(self.data_list_crawler)

        self.redis = Redis(host="tz6.zhangyupai.net", password="Lz@12@12@julai", port=6379, db=8)
        self.mylog = getLoger(self.name + '.log')

        self.db1 = pymysql.connect(self.host, self.user,
            self.password, self.database4, charset='utf8')
        self.cursor1 = self.db1.cursor()
        sql = 'select word from words where del_flag = 0 ORDER BY choose_flag ASC'
        self.cursor1.execute(sql)
        self.word_data = set([i[0].replace("+", "") for i in self.cursor1.fetchall()])

        conn = pymysql.connect(host='120.26.211.213', user='julai01', password='Zycj@2020688', database='news_caiji',
             charset='utf8mb4', )
        sql = '''select name from weixin where type =1 OR wxcat = 1'''

        with conn.cursor() as cur:
            cur.execute(sql)
            all_data_exclude = [i[0] for i in cur.fetchall()]

        self.all_media_data_list = all_data_exclude


    def start_requests(self):



        for name in self.word_data:



            url = f'https://weixin.sogou.com/weixin?query={name}&_sug_type_=-1&tro=on&s_from=input&_sug_=y&type=2&page=1&ie=utf8'

            yield scrapy.Request(url,callback=self.parse,dont_filter=True)



    def parse(self, response):

        all_data_str = []
        yesterday = datetime.today() + timedelta(-1)

        yesterday_str = yesterday.strftime('%Y%m%d')
        content_list = response.xpath("//ul[@class='news-list']/li")


        for info in content_list:

            re_time = info.xpath(".//span[@class='s2']/script/text()").get()

            re_time_int = re.findall(r'\d+', str(re_time))[0]

            Other_time = time.localtime(int(re_time_int))
            post_time_s = time.strftime('%Y%m%d', Other_time)
            titles = ''.join(info.xpath('.//h3/a//text()').getall()).strip()
            title = ''.join(re.findall(u'[\u4e00-\u9fa5]', titles))
            meida = info.xpath('.//div[@class="s-p"]/a/text()').get().strip()

            all_data_str.append(post_time_s)
            ex = self.redis.sadd('crawled_title', title+meida)
            if ex==1 and post_time_s >=yesterday_str and meida not in self.all_media_data_list:
                print('新数据产生中。。。。。。。。。',title,meida)
                link = 'https://weixin.sogou.com' + info.xpath(".//h3/a/@href").get()

                yield  scrapy.Request(link,callback=self.get_link,
                meta={"title":title,'meida':meida,'post_time_s':post_time_s})

        next_page = response.xpath("//div[@class = 'p-fy']/a[text()='下一页']")

        max_str_date = max(all_data_str)

        if next_page and max_str_date >= yesterday_str:
            next_url_text = response.xpath("//div[@class = 'p-fy']/a[text()='下一页']/@href").get()

            next_url = response.urljoin(next_url_text)

            yield scrapy.Request(next_url,callback=self.parse,meta={'meida':meida},
               )

    def get_link(self,response):
        meida = response.meta['meida']
        title = response.meta['title']
        post_time_s = response.meta['post_time_s']
        index_url = ''.join(re.findall(r"url \+= '(.*?)';", response.text))
        data = CeshiItem(title=title, media=meida, post_time=post_time_s,url=index_url)
        yield data
        self.redis.lpush('SGurl:start_urls', index_url)

        self.mylog.info((meida,index_url))
