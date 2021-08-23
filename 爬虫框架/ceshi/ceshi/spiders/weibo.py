import json
import re
import time
from datetime import datetime, timedelta

import pymysql
import scrapy
from redis import Redis
from scrapy.utils.project import get_project_settings

from ..tools import getLoger


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']
    # start_urls = ['http://weibo.com/']
    custom_settings = {
        'CONCURRENT_REQUESTS': 2,

        'DOWNLOADER_MIDDLEWARES':{
        'ceshi.middlewares.locationproxy':543
    }

    }


    def __init__(self, **kwargs):


        get_setting = get_project_settings()
        self.host = get_setting.get("MYSQL_HOST3")
        self.user = get_setting.get("MYSQL_USER3")
        self.password = get_setting.get("MYSQL_PASSWORD3")
        self.database4 = get_setting.get("MYSQL_DATABASE4")
        self.database = get_setting.get("MYSQL_DATABASE5")
        self.db = pymysql.connect(self.host, self.user,
        self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()
        self.redis = Redis(host="tz6.zhangyupai.net", password="Lz@12@12@julai", port=6379, db=8)
        self.mylog = getLoger(self.name + '.log')

        self.db1 = pymysql.connect(self.host, self.user,
            self.password, self.database4, charset='utf8')
        self.cursor1 = self.db1.cursor()
        sql = 'select word from words where del_flag = 0 ORDER BY choose_flag ASC'
        self.cursor1.execute(sql)
        self.word_data = set([i[0].replace("+","") for i in self.cursor1.fetchall()])



    def start_requests(self):


        jijin_list = list(self.word_data)
        print(jijin_list)

        for name in jijin_list:

            for page in [1,2,3,4]:
                base_url = f'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D{name}%26t%3D0&page_type=searchall&page={page}'

                yield scrapy.Request(base_url,callback=self.parse,meta={'name':name})


    def parse(self, response):
        name = response.meta['name']
        total_content = json.loads(response.text).get('data').get('cards')
        # content_list = total_content.get('card_group')
        for items in total_content:
            total_boxes = items.get('mblog')
            id_ = total_boxes.get('bid')
            time_url = 'https://m.weibo.cn/statuses/show?id={}'.format(id_)
            ex = self.redis.sadd('crawledwb_url', time_url+'&weibo')
            if ex == 1:
                if 'iNone' not in time_url:
                    print({"time_url": time_url, 'name': name})
                    self.redis.lpush("WBDATA:start_data", {"time_url": time_url, 'name': name})
            else:

                print('数据已经存在....')

    #         yield scrapy.Request(time_url,callback=self.parse2,meta={"bid":id_,
    #                                                                  'name':name},dont_filter=True)
    #
    # def parse2(self, response):
    #     bid = response.meta['bid']
    #     name = response.meta['name']
    #     yesterday = datetime.today() + timedelta(-1)
    #     yesterday_str = yesterday.strftime('%Y%m%d')
    #     created_time = json.loads(response.text).get("data").get(
    #                 "created_at")
    #     m_time = time.mktime((time.strptime(created_time, "%a %b %d %H:%M:%S +0800 %Y")))
    #     timeArray = time.localtime(m_time)
    #     Create_time = time.strftime("%Y%m%d", timeArray)  # 微博发布时间
    #     if Create_time >= str(yesterday_str):
    #         weibo_url = 'https://m.weibo.cn/status/{}?mblogid={}'.format(bid, bid)
    #         format_text = json.loads(response.text).get("data").get("text")
    #         screen_name = json.loads(response.text).get("data").get("user").get("screen_name")
    #         content = re.compile(u'[\U00010000-\U0010ffff]').sub(u'', format_text) + '{}'.format(name)
    #         titles =format_text.split('，')[0].strip()
    #         title = re.compile(u'[\U00010000-\U0010ffff]').sub(u'', titles)
    #         print(title,weibo_url)
