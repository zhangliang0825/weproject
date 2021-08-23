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
from loguru import logger

# logger.add('webtt数据记录.log',retention='2 days')

class WebttSpider(scrapy.Spider):
    name = 'webtt'
    #网页端的资讯信息
    allowed_domains = ['m.toutiao.com']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

  # 'cookie': ' PIXIEL_RATIO=1.5; sid_guard=6d59bafe68b1d4985bbafd8acc5f815a%7C1594191164%7C5184000%7CSun%2C+06-Sep-2020+06%3A52%3A44+GMT; UM_distinctid=1735a6621107d5-00bb1f0a596c86-b7a1334-e1000-1735a662112a2c; CNZZDATA1274463548=409357553-1594944740-%7C1594944740; __utmz=24953151.1599121320.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); FRM=new; __utma=24953151.1663346515.1599121320.1600935555.1601188260.7; tt_webid=6877724130952234504; MONITOR_WEB_ID=6877724130952234504; WIN_WH=1280_578; tt_webid=6835446038360000013',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': ' 1',
  'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
},
        'DOWNLOADER_MIDDLEWARES': {
            'toutiao.middlewares.UserAgentDownloadMiddleware': None,
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
        self.word_data = ['华夏幸福','包商银行','中信信诚','博时基金',"基金",'长信基金','嘉实基金','国泰元鑫','国泰基金','富国基金','南方基金','招商基金','银华基金','新华基金','平安基金','兴全基金','兴证全球',
                          '中欧基金','鹏华基金','鹏华基金','中邮基金','华夏基金','易方达','华安基金','华商基金','民生加银','富安达基金','中信保诚','信诚基金','国海富兰克林','东证资管','东方红基金']

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

    @logger.catch
    def parse_2(self, response):

        type_ = response.meta['type_']

        Filter_data = MapCompose(json.loads, SelectJmes('dom'))

        # # 生成一个规则
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
                toutiao_url = f'https://www.toutiao.com/i{Single_id}/'
            self.redis.lpush('TTurl:start_urls', toutiao_url)
            logger.debug((toutiao_url,meida_name,media_code,Single_id))
            print(toutiao_url,meida_name,media_code,Single_id)
            if meida_name == '' or meida_name =='金融界':
                continue
            if meida_name not in self.data_list:
                sql = 'insert into media(media,post_type,link) values (%s,%s,%s)'
                self.cursor.execute(sql,(meida_name,1,media_code))
                self.db.commit()
                print(meida_name,'已插入库中.......')
                self.data_list.append(meida_name)




                # all_data = str(All_Data_List[0]).replace('\"', '')
        # doc = pq(all_data)
        #
        # data_list = doc("div.grid div.cs-view")
        # for item in data_list.items():
        #     data_item = item.attr('data-log-click')
        #     if data_item:
        #         content_type = json.loads(data_item).get("type")
        #         cardid = json.loads(data_item).get("cardid")
        #         if content_type == 'weitoutiao':
        #             toutiao_url = f'https://www.toutiao.com/a{cardid}'
        #
        #         else:
        #             toutiao_url = f'https://www.toutiao.com/i{cardid}'
        #
        #         self.redis.lpush('TTurl:start_urls', toutiao_url)
        #         print(toutiao_url)
