# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.loader import ItemLoader
import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
import re











class SpiderRedisItem(scrapy.Item):
    bizname = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    html = scrapy.Field()
    str_date = scrapy.Field()
    post_time = scrapy.Field()
    media_orig = scrapy.Field()
    content_url = scrapy.Field()
    username = scrapy.Field()
    biz = scrapy.Field()
    media = scrapy.Field()