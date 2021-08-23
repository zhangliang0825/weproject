# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from time import sleep

import requests
from lxml import etree
import json,base64
from datetime import datetime

# def redis_data(now_time, title, url, info):
#
#     data = {
#        'ts': now_time,
#        'title': str(base64.b64encode(title.encode('utf-8')), 'utf-8'),
#        'link': str(base64.b64encode(url.encode('utf-8')), 'utf-8'),
#        'info': info,
#        'spider': "paper"
#     }
#     res = requests.get('http://tz4.zhangyupai.net:7379/LPUSH/jj_spiders/' + json.dumps(data), timeout=20).text
#     print(res)

class PaperPipeline:
    def __init__(self):
        self.api = 'http://tz4.zhangyupai.net:81/mobile/import_xtnews1.php'

    def post(self, info):
        title, content, summary, media_orig, reporter, content_url, str_date, name,jj_name = info
        data = {'title': title, 'content': content, 'summary': summary, 'media_orig': media_orig, 'reporter': reporter, 'content_url': content_url, 'str_date': str_date, 'spider_channel': 'scrapy', 'spider': name,'jj_name':jj_name}
        requests.post(self.api, data=data)
        sleep(0.1)

    def process_item(self, item, spider):
        url = item['url']
        date = item['date']
        reporter = item['reporter']
        title = item['title']
        media_orig = item['media_orig']
        content = '[xt]' + item['content']

        if '<' in item['content'] and '>' in item['content']:
            html = etree.HTML(item['content'])
            text = ''.join(i for i in html.xpath('//text()') if i).strip()
            if len(text) > 80:
                abstract = text[:80]
            else:
                abstract = text[:int(0.5*len(text))]
            if abstract:
                info = (title, content, abstract, media_orig, reporter, url, date, spider.name)
                self.post(info)

        return item


class PaperPipeline2:
    def __init__(self):
        self.api = 'http://tz4.zhangyupai.net:81/mobile/import_gbpost.php'

    def process_item(self, item, spider):
        url = item['url']
        jj_name = item['jj_name']
        date = item['date']
        reporter = item['reporter']
        title = item['title']
        media = item['media']  # media: 发布网站
        media_orig = ''  # media_orig: 源网站
        if 'media_orig' in item:
            media_orig = item['media_orig']
        post_type = 0
        if 'post_type' in item:
            post_type = item['post_type']
        content = '[paper]' + item['content']
        data = {'title': title, 'content_url': url, 'post_type': post_type, 'media': media, 'media_orig': media_orig, 'reporter': reporter, 'str_date': date, 'spider_name': spider.name, 'content': content,'jj_name':jj_name}
        # redis_data(datetime.now().strftime("%m%d%H%M%S"), title, url, spider.name)
        requests.post(self.api, data=data)
