# -*- coding: utf-8 -*-
import csv
import re
import time
from ..items import SpiderRedisItem
import pymysql
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from lxml import etree
class SougouSpider(RedisSpider):
    custom_settings = {'REDIS_URL': 'redis://root:Lz@12@12@julai@tz6.zhangyupai.net:6379/10',
                        'DEFAULT_REQUEST_HEADERS':{'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Host':'mp.weixin.qq.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.4.3; zh-cn; HTC 802w Build/KTU84L) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025489 Mobile Safari/533.1 MicroMessenger/6.3.13.49_r4080b63.740 NetType/WIFI Language/zh_CN',

                       },
                       'DOWNLOAD_DELAY' : 3,


    }

    redis_key = 'SGurl:start_urls'

    name = 'sougou'
    allowed_domains = ['sougou.com']



    def make_requests_from_url(self, url):
        return scrapy.Request(url, method='GET',
                   callback=self.parse,)


    def parse(self, response):
        if '分享一篇文章。' not in response.text:
            link = response.url
            soup_doc = response.xpath('//div[@class="rich_media_content "]//text()')
            if soup_doc:
                re_time = re.findall(re.compile(r'var ct = (.*?);'), str(response.text))[0].strip('"')

                Other_time = time.localtime(int(re_time))
                post_time = time.strftime('%Y%m%d', Other_time)  # 发布时间

                title = response.xpath("//div[@id='img-content']/h2[@class='rich_media_title']/text()").get().strip()
                meida = response.xpath("//span[@class='rich_media_meta rich_media_meta_nickname']/a/text()").get().strip()

                media_ori = response.xpath("//p[@class='original_primary_card_tips']/span/text()")

                response = etree.HTML(response.text)
                parent = response.xpath('''//div[@class='rich_media_content ']''')[0]
                for r in parent.xpath('//a'):
                    r.getparent().remove(r)
                soup_doc = ''.join(parent.xpath("//div[@class='rich_media_content ']//text()"))
                soup_doc = re.sub(r'\s+', '', soup_doc)
                content = re.compile(u'[\U00010000-\U0010ffff]').sub(u'', soup_doc)
                html_pattern = response.xpath("//div[@id='js_article']")[0]

                html = etree.tostring(html_pattern, encoding="utf-8", pretty_print=True, method="html").decode('utf8')
                # html = etree.tostring(html_pattern, encoding="utf-8", pretty_print=True, method="html").decode('utf8')
                if media_ori:
                    media_ori = re.search('以下文章来源于(.*)', str(media_ori.get().strip())).group(1)

                else:
                    media_ori = meida
            else:
                content = response.xpath("//p[@class='share_notice']/text()")

            if  '长发垂肩计回复后恢复君' not in content:

                biz = re.findall(r'var appuin = (.*?);', str(response.text))
                if biz:
                    biz = biz[0].strip('"').strip('""||"')
                else:
                    biz = ''

                All_data = SpiderRedisItem(biz=biz,title=title, content=content,html=html,
                    media_orig=media_ori, str_date=post_time, content_url=link, username=meida,bizname = meida)
                yield All_data
