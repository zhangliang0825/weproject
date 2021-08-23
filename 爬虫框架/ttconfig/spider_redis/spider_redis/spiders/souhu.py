# -*- coding: utf-8 -*-
import requests
import scrapy
import re
import json
from lxml import etree
from scrapy import Request
# from scrapy.loader.processors import MapCompose,SelectJmes,Join,TakeFirst
from ..items import SpiderRedisItem
import datetime, time
from scrapy_redis.spiders import RedisSpider


# from ..get_cookies import TransCookie

today = datetime.datetime.now()
end = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')


# RedisSpider
class SouhuSpider(RedisSpider):
    custom_settings = { 'REDIS_URL' : 'redis://root:Lz@12@12@julai@tz6.zhangyupai.net:6379/8'}
    name = 'souhu'
    allowed_domains = ['www.souhu.com']

    redis_key = 'SHurl:start_urls'
    def __init__(self):
        self.for_num = 0

    #
    #

    def make_requests_from_url(self, url):
        if 'None' not in url:

                return Request(url, method='GET',
                     meta={
                        'dont_redirect': True,
                        'handle_httpstatus_list': [307],

                    })

    # def start_requests(self):
    #     url = 'https://www.sohu.com/a/466209149_120466746'
    #     yield scrapy.Request(url,callback=self.parse,dont_filter=True)



    def parse(self, response):
        url = response.url
        if 'picture' not in url:
            # with open('11.html','w',encoding='utf8') as f:
            #     f.write(response.text)
            # #
            # # print(1111111111111111111111111111)
            # # time.sleep(8)
            # title = ''.join(response.xpath("//div[@class='text-title']//h1//text()|//div[@class='content-info']/h1/text()").getall())
            # title_ = re.sub(r'\s+','',title).strip('原创')
            # content_ = ''.join(response.xpath("//article[contains(@class,'article')]/p//text()").getall())+title_
            #             media = response.xpath(
            #     "//div[@class='user-info']/h4/a/text()|//p[@class='info']//span[@class='name']/text()").get()
            #
            # time_ = response.xpath("//div[@class='text-title']//span[@class='time']/text()|//span[@class='timer']//text()").get().replace('.','-')
            title = response.xpath("//meta[@property='og:title']/@content").get()
            if '_' in title:
                title_ = ''.join(title.strip().split('_')[:-1])
            else:
                title_ = title
            content_ =  ''.join(response.xpath("//article[contains(@class,'article')]/p//text()").getall()).replace('返回搜狐，查看更多责任编辑：','').strip()+title_
            time_ = response.xpath("//meta[@property='og:release_date']/@content").get().replace('.', '-')
            media = response.xpath("//meta[@name='mediaid']/@content").get()
            if not media  and title_!='':
                media = '搜狐新闻'
            else:
                media = media
            if media:
                All_data = SpiderRedisItem(title=title_, content=content_,
                            media_orig=media, str_date=time_, content_url=url, username=media)

                yield All_data
            else:
                print('1111111111111出于....数据有问题..')