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
from datetime import datetime,timedelta
# from ..get_cookies import TransCookie

# today = datetime.datetime.now()
# end = datetime.datetime.strftime(today, '%Y-%m-%d %H:%M:%S')


# RedisSpider
class SouhuSpider(RedisSpider):
    custom_settings = {'REDIS_URL': 'redis://root:Lz@12@12@julai@tz6.zhangyupai.net:6379/8'}
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']

    redis_key = 'WBDATA:start_data'

    def __init__(self):
        self.for_num = 0

    def make_request_from_data(self, data):
        id_data = eval(data.decode('utf8'))

        url = id_data['time_url']
        key_name = id_data['name']
        return Request(url, method='GET',
            meta={
                'dont_redirect': True,
                'handle_httpstatus_list': [307],
                'key_name':key_name

            })

    def parse(self, response):
        key = response.meta['key_name']
        url = response.url
        bid = re.search(r'id=(.*)',url).group(1)
        yesterday = datetime.today() + timedelta(-1)
        yesterday_str = yesterday.strftime('%Y%m%d')
        created_time = json.loads(response.text).get("data").get(
                    "created_at")
        m_time = time.mktime((time.strptime(created_time, "%a %b %d %H:%M:%S +0800 %Y")))
        timeArray = time.localtime(m_time)
        Create_time = time.strftime("%Y%m%d", timeArray)  # 微博发布时间
        if Create_time >= str(yesterday_str):
            weibo_url = 'https://m.weibo.cn/status/{}?mblogid={}'.format(bid, bid)
            _text = json.loads(response.text).get("data").get("text")
            format_text = re.sub(r'<.*?>','',_text)
            screen_name = json.loads(response.text).get("data").get("user").get("screen_name")
            content = re.compile(u'[\U00010000-\U0010ffff]').sub(u'', format_text) + '{}'.format(key)
            titles =format_text.split('，')[0].strip()
            title = re.compile(u'[\U00010000-\U0010ffff]').sub(u'', titles)
            All_data = SpiderRedisItem(title=title, content=content,
            media_orig=screen_name, str_date=Create_time, content_url=weibo_url, username=screen_name)

            yield All_data
