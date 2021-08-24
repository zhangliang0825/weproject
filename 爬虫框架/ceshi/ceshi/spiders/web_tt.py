# -*- coding: utf-8 -*-
import json
import re

from pyquery import PyQuery as pq
import pymysql
import scrapy
from redis import Redis
from scrapy.loader.processors import SelectJmes, MapCompose
from scrapy.utils.project import get_project_settings
from scrapy import Selector
from ..tools import getLoger

class WebttSpider(scrapy.Spider):
    name = 'web_tt'
    #网页端的资讯信息
    allowed_domains = ['m.toutiao.com']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {'Accept':'application/json',

'Connection':'keep-alive',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'tt_webid=6999810541595182599; WIN_WH=1280_577; PIXIEL_RATIO=1.5; FRM=new; s_v_web_id=verify_6b5559a9c1af5a7c2813150f100c90e4; MONITOR_WEB_ID=6999810541595182599; _signature=_02B4Z6wo00f01LqQFkwAAICAOpLsDeTlACS6sBLAAE-Fa8; ttcid=9becd88c89c542c39e76842f2f0abe9276; tt_scid=a.7T0OfXUOWzXU6ybFxu-43KdUiQCJPmYmhTPRIuqV4xemDZEpPl2MU7VFlURuVzc9ce',
'Host':'m.toutiao.com',
'Referer':'https://m.toutiao.com/search?keyword=%E5%98%89%E5%AE%9E%E5%9F%BA%E9%87%91&pd=information&original_source=&in_ogs=',
'sec-ch-ua':'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
'sec-ch-ua-mobile':'?0',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
            

},
        'DOWNLOADER_MIDDLEWARES': {
            # 'toutiao.middlewares.UserAgentDownloadMiddleware': None,
            'ceshi.middlewares.GetFailedrequsts': 544
            # 'toutiao.middlewares.RandomProxy': 600,
        },
        'ITEM_PIPELINES': {

            'toutiao.pipelines.BaiDuPipeline': None,

        }}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cookies = get_project_settings().get("COOKIES_TT_WEB")

        self.redis = Redis(host="tz6.zhangyupai.net", password="Lz@12@12@julai", port=6379, db=8)
        get_setting = get_project_settings()
        self.host = get_setting.get("MYSQL_HOST3")
        self.user = get_setting.get("MYSQL_USER3")
        self.password = get_setting.get("MYSQL_PASSWORD3")
        self.database = get_setting.get("MYSQL_DATABASE4")
        self.db = pymysql.connect(self.host, self.user,
            self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()
        sql = 'select word from words where del_flag = 0 ORDER BY choose_flag ASC'
        self.cursor.execute(sql)
        self.word_data = set([i[0].replace("+","") for i in self.cursor.fetchall()])
        print(self.word_data)
        self.mylog = getLoger(self.name + '.log')
           # self.word_data = ['嘉实归凯','拉夏','ST拉夏','拉夏贝尔',"基金",'交银','交银施罗德','长信基金','嘉实基金','国泰元鑫','国泰基金','富国基金','南方基金','招商基金','银华基金','新华基金','平安基金','兴全基金','兴证全球',
    #                   '中欧基金','鹏华基金','鹏华基金','中邮基金','华夏基金','易方达','华安基金','华商基金','民生加银','富安达基金','中信保诚','信诚基金','国海富兰克林']

    def start_requests(self):
        self.db = pymysql.connect(self.host, self.user,
            self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()
        sql = '''select distinct media from media'''
        self.cursor.execute(sql)
        self.data_list = [i[0] for i in self.cursor.fetchall()]
        for type_ in ['information','weitoutiao']:
            for word in self.word_data:
                for i in range(0,5):
                    page = i*10
                    if type_ == 'weitoutiao':
                        url = f'https://m.toutiao.com/search/?keyword={word}&pd={type_}&source=&traffic_source=&original_source=&in_tfs=&in_ogs=&format=json&count=10&offset={page}&from=news&start_index=10&index_resource=&filter_vendor=&filter_period=&min_time=&max_time=&from_search_id'
                    else:
                        url = f'https://m.toutiao.com/search/?keyword={word}&pd={type_}&source=&traffic_source=&original_source=&in_tfs=&in_ogs=&format=json&count=10&offset={page}&from=news&start_index=10&index_resource=&filter_vendor=&filter_period=&min_time=&max_time=&from_search_id'

                    yield scrapy.Request(url, callback=self.parse_2, cookies=self.cookies, dont_filter=True,meta={'type_':type_})


    def parse_2(self, response):

        type_ = response.meta['type_']

        Filter_data = MapCompose(json.loads, SelectJmes('dom'))

        All_Data_Json = Filter_data(response.text)[0]
        response = Selector(text=All_Data_Json)
        gid = MapCompose(json.loads, SelectJmes("gid"))
        All_data_list = response.xpath("//div[@class = 'result-content']")
        for info in All_data_list:
            Single_data = info.xpath('./@cr-params').get()
            Single_id = gid(Single_data)[0]
            if type_ == 'weitoutiao':
                meida_name = info.xpath(".//div[@class ='text-m word-line-1']/text()").get()
                meida_url = info.xpath('.//div[@class="cs-view cs-view-block"]/a/@href').get()
                if '%2Fgroup%2F' in meida_url:
                    continue
                if meida_url:

                    media_code = re.search(r'Fuser%2F(.*?)%2F&log', meida_url).group(1)
                else:
                    media_code = ''
                toutiao_url = f'https://www.toutiao.com/w/a{Single_id}'
            else:
                meida_name = ''.join(info.xpath(".//div[contains(@class,'flex-shrink-1')]/div[contains(@class,'word-line-1')]//text()").getall())
                media_code = ''
                toutiao_url = f'https://toutiao.com/i{Single_id}/'
            ex = self.redis.sadd('crawledtt_url', toutiao_url)
            if ex == 1:
                if 'iNone' not in toutiao_url:
                    self.redis.lpush('TTurl:start_urls', toutiao_url)
            else:
                print('数据已存在...')
            self.mylog.info((toutiao_url,meida_name,media_code,Single_id))

            if meida_name == '' or meida_name =='金融界':
                continue
            if meida_name not in self.data_list:
                sql = 'insert into media(media,post_type,link) values (%s,%s,%s)'
                self.cursor.execute(sql,(meida_name,1,media_code))
                self.db.commit()

                self.data_list.append(meida_name)
