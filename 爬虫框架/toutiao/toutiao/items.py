# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.loader import ItemLoader
import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
import re




class CententItemLoader(ItemLoader):
    default_output_processor  = TakeFirst()



class SpiderRedisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    str_date = scrapy.Field()
    media_orig = scrapy.Field()
    media_id = scrapy.Field()
    content_url = scrapy.Field()
    post_type = scrapy.Field()
    media = scrapy.Field()
    readnum = scrapy.Field()
    likenum = scrapy.Field()
    oldlikenum = scrapy.Field()
