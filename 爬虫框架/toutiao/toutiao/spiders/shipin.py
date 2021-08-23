import json
import re
import time

from ..items import SpiderRedisItem
import requests
from pyquery import PyQuery as pq
import pymysql
import scrapy

from redis import Redis
from scrapy.loader.processors import SelectJmes, MapCompose
from scrapy.utils.project import get_project_settings
from scrapy import Selector
from loguru import logger
from datetime import datetime,timedelta

yesterday = datetime.today()+timedelta(-1)
yesterday_str = yesterday.strftime('%Y%m%d')

class WebttSpider(scrapy.Spider):
    name = 'shipin'
    #网页端的资讯信息
    allowed_domains = ['api.youwant.cn']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {

  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56'
},
        'DOWNLOADER_MIDDLEWARES': {
            'toutiao.middlewares.UserAgentDownloadMiddleware': None,
            # 'toutiao.middlewares.RandomProxy': 600,
        },
        'ITEM_PIPELINES': {

            'toutiao.pipelines.ToutiaoPipeline': 503,

        }}

    def __init__(self, **kwargs):
        self.cookies = {
            '_data_chl':'key=BaiduOrginal',
            'YOUWANTDATA':'UserId=2f50f7e3698d12a4&Password=cab4121faab3ead3a6c6af46946a093d&ChildUserId=103dad732c906557&ClientId=c05ab439cc014accb710aa0f0ea0f9ed',
            'ASP.NET_SessionId':'kapx1ezcokinewt01zkimoz4'
        }

    def start_requests(self):
        # statr_url = 'http://api.youwant.cn/v1/video/getBloggerVideoList?pageSize=10&pageIndex=0&bloggerId=5900&sortType=3'
        word_list = ['嘉实基金V视界',
'新华基金','华安基金','景顺长城','中信保诚','博时基金','嘉实基金','南方基金','天弘基金','兴证全球基金','建信基金','汇添富基金','鹏华基金','民生加银基金','交银施罗德','银华基金','招商基金','天弘基金','华安基金','鹏华基金','中欧基金','东方红资产管理','国泰元鑫',
'富国基金','平安基金','中邮基金','东证资管','新华基金','华商基金','华夏基金', '易方达基金','工银瑞信基金','海富通基金','华宝基金','高毅资产'
#             '富国基金',
           ]
        for word in word_list:
            time.sleep(1.5)
            statr_url = 'http://api.youwant.cn/v1/dashBoard/search?keyword={}&_=1612281159235'.format(word)

            # cookies = {'Cookie': '_data_chl=key=BaiduOrginal; UWANTDATA=UserId=2f50f7e3698d12a4&Password=bb6d36803a559903f594acab88125dbb&ChildUserId=103dad732c906557&ClientId=f91eb0c3c9f44eb8a3c4b5e6b65b9668; ASP.NET_SessionId=4dkhre4n3uf0phi531mqzogl; ASP.NET_SessionId=0oygv2wjldpf0hylpmuueduu'}
            yield scrapy.Request(statr_url,callback=self.parse1,cookies=self.cookies,dont_filter=True,meta={'keywords':word})

    def parse1(self, response):
        word = response.meta['keywords']
        data_list = json.loads(response.text).get('Data').get('BloggerList')
        for item in data_list:
            BloggerId = item.get('BloggerId')
            # 'http://api.youwant.cn/v1/video/getBloggerVideoList?pageSize=10&pageIndex=1&bloggerId=5900&sortType=3&begin=1609776000&end=1612368000&durationType=-1&linkState=-1&firstCategoryId=0&_=1612402024136'
            # start_url = f'http://api.youwant.cn/v1/video/getBloggerVideoList?pageSize=10&pageIndex=1&bloggerId={BloggerId}&sortType=3&begin=1617033600&end=1619625600&durationType=-1&linkState=-1&firstCategoryId=0&topicId=0&_={int(time.time()*1000)}'
            start_url = f'http://api.youwant.cn/v1/blogger/getVideoList?pageSize=10&pageIndex=2&bloggerId={BloggerId}&sortType=3&begin=1625846400&end=1628438400&durationType=-1&linkState=-1&firstCategoryId=0&topicId=0&_={int(time.time()*1000)}'
            print(start_url)
            # statr_url = f'http://api.youwant.cn/v1/video/getBloggerVideoList?pageSize=10&pageIndex=1&bloggerId=&sortType=3&begin=1609776000&end=1612368000&durationType=-1&linkState=-1&firstCategoryId=0&_=1612402024136'
            #             ='http://api.youwant.cn/v1/video/getBloggerVideoList?pageSize=10&pageIndex=1&bloggerId=5900&sortType=3&begin=1609776000&end=1612368000&durationType=-1&linkState=-1&firstCategoryId=0&_=1612402024136'
            yield scrapy.Request(start_url, callback=self.parse, cookies=self.cookies, dont_filter=True,meta={'keywords':word})

    def parse(self,response):
        word = response.meta['keywords']
        for item in json.loads(response.text).get('Data').get('ItemList'):
            title = item.get("Description")
            title = re.compile(u'[\U00010000-\U0010ffff]|\s+').sub(u'',title)
            content = title+word+'基金'
            PubTimeDesc = item.get("DateCode")
            VideoIdKey = item.get("VideoIdKey")
            LikeCount = item.get("LikeCount")
            ForwardCount = item.get("ForwardCount")
            CommentCount = item.get("CommentCount")
            DurationDesc = item.get("DurationDesc")

            if int(yesterday_str) <=PubTimeDesc:
                response = requests.get('http://api.youwant.cn/v1/video/getVideoUrl?videoId=44034813&key=8fd3cd&dateCode=20210804&_=1628471078343')
                video_url = item.get("Url")+'&==='
                all_data = SpiderRedisItem(title=title, content = content,
                str_date= PubTimeDesc,media_orig = word,
                    readnum =ForwardCount,likenum=LikeCount, oldlikenum = CommentCount,
                    content_url = video_url)
                yield all_data





