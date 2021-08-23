# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    media = scrapy.Field()
    jj_name = scrapy.Field()
    media_orig = scrapy.Field()
    reporter = scrapy.Field()
    content = scrapy.Field()
    post_type = scrapy.Field()
