# -*- coding: utf-8 -*-
import copy

import scrapy
import re
import json
import logging
from ..tools import getLoger
# from scrapy.loader.processors import MapCompose,SelectJmes,Join,TakeFirst
from ..items import SpiderRedisItem
import datetime,time
from scrapy_redis.spiders import RedisSpider
from scrapy.utils.project import get_project_settings

today = datetime.datetime.now()
end = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')
#RedisSpider
class ToutiouSpider(RedisSpider):
    custom_settings = {'REDIS_URL': 'redis://root:Lz@12@12@julai@tz6.zhangyupai.net:6379/8'
                       ,'DOWNLOAD_DELAY':0.8,
                       'CONCURRENT_REQUESTS' : 12
                       }
    name = 'toutiao'
    allowed_domains = ['www.toutiao.com']
    # start_urls = ['https://www.toutiao.com/a6839554778373030414']


    cookies = get_project_settings().get('COOKIES_TT')



    redis_key = 'TTurl:start_urls'
    def __init__(self):
        self.for_num = 0
        self.mylog = getLoger(self.name + '.log')



    def make_requests_from_url(self, url):


            if 'None' not in url:

                id_tt = re.search(r'(\d+)',url).group(1)
                new_url = 'https://m.toutiao.com/i{}/info/'.format(id_tt)
                meta = {
                    'dont_redirect': True,
                    'handle_httpstatus_list': [301],
                    'source_url': id_tt
                }
                return scrapy.Request(new_url,method='GET',
                    cookies=self.cookies,meta=copy.deepcopy(meta))
   

    def parse(self, response):

        source_url = response.meta['source_url']
        success = json.loads(response.text).get("success")
        if success:
            all_data = json.loads(response.text).get("data")
            group_source = all_data.get("group_source")


            if  group_source ==5:#微头条
                thread = all_data.get("thread").get("thread_base")
                content = thread.get("content")
                title = thread.get("title",content)
                create_time = thread.get("create_time")
                time_ = time.localtime(int(create_time))
                time_ = time.strftime('%Y-%m-%d %H:%M:%S', time_)
                media = thread.get("user").get("info").get("name")
                source_url = 'https://www.toutiao.com/w/a{}/'.format(source_url)

            elif group_source == 23:
                comment = all_data.get('comment').get('comment_base')
                title = comment.get('content')
                content_ = all_data.get('comment')
                if 'origin_thread' in content_:
                    content = content_.get('origin_thread').get('title')
                elif 'origin_group' in content_:
                    content = content_.get('origin_group').get('title')
                else:
                    content = ''
                content = title+content
                create_time = comment.get('create_time')
                time_ = time.localtime(int(create_time))
                time_ = time.strftime('%Y-%m-%d %H:%M:%S', time_)
                media = comment.get("user").get("info").get("name")
                source_url = 'https://www.toutiao.com/w/a{}/'.format(source_url)
            else:
                title = all_data.get("title")
                content = all_data.get("content")
                publish_time = all_data.get("publish_time")
                time_ = time.localtime(int(publish_time))
                time_ = time.strftime('%Y-%m-%d %H:%M:%S', time_)
                media = all_data.get("detail_source")
                source_url = 'https://www.toutiao.com/i{}/'.format(source_url)
            All_data = SpiderRedisItem(title=title, content=content,
                media_orig=media, str_date=time_, content_url=source_url, username=media)

            yield All_data
        else:

            yield scrapy.Request(response.url,cookies=self.cookies,callback=self.parse,meta={  'source_url':source_url})


