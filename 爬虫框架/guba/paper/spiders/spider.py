# -*- coding: utf-8 -*-
import sys
import time
import hashlib
import datetime
import json
import re
import requests
import demjson
import scrapy
from lxml import etree
from lxml import html
from readability import Document  # pip install readability-lxml
from urllib.parse import urljoin
from retrying import retry
from ..items import PaperItem
from ..log_config import logger
from html.parser import HTMLParser
from collections import defaultdict
from ..urls import old_urls, today, yesterday, old_urls_ano,old_urls_from_jijin_urls
# from loguru import logger



class guba(scrapy.Spider):
    name = "eastmoneyguba"

    def __init__(self):


        self.header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'emshistory=%5B%22%E5%B7%A5%E9%93%B6%E7%91%9E%E4%BF%A1%22%2C%22%E4%B8%AD%E6%AC%A7%E5%9F%BA%E9%87%91%22%2C%22300ETF%22%2C%22%E5%98%89%E5%AE%9E300ETF%22%2C%22%E5%85%B4%E5%85%A8%22%2C%22%E5%9F%BA%E9%87%91%E6%97%A5%E6%8A%A5%E4%B8%A8%E4%B8%AD%E6%A6%82%E8%82%A1%E5%9B%9E%E5%BD%92%EF%BC%8C%E8%BF%99%E7%B1%BB%E5%9F%BA%E9%87%91%E6%9C%80%E5%8F%97%E7%9B%8A%22%2C%22%E7%8E%8B%E5%81%A5%22%2C%22%E4%B8%AD%E6%AC%A7%20%E7%8E%8B%E5%81%A5%22%2C%22%5C%22%E4%B8%AD%E6%AC%A7%20%E7%8E%8B%E5%81%A5%5C%22%22%2C%22%5C%22%E4%B8%AD%E6%AC%A7%2B%E7%8E%8B%E5%81%A5%5C%22%22%2C%22%E4%B8%AD%E6%AC%A7%2B%E7%8E%8B%E5%81%A5%22%2C%22%E4%B8%AD%E6%AC%A7%22%2C%22%E4%B8%AD%E6%AC%A7%E5%9F%BA%E9%87%91%20%E7%8E%8B%E5%81%A5%22%2C%22%E4%B8%AD%E6%AC%A7%E5%9F%BA%E9%87%91%2B%E7%8E%8B%E5%81%A5%22%2C%22%E5%98%89%E5%AE%9E%E5%9F%BA%E9%87%91%22%5D; st_si=07624150866665; st_asi=delete; qgqp_b_id=eacfbe941db39c469c41efc8fc02d264; st_pvi=09136297881648; st_sp=2020-05-12%2021%3A52%3A47; st_inirUrl=http%3A%2F%2Ffund.eastmoney.com%2F005275.html; st_sn=6; st_psi=20201111084806952-117001300541-3300372242',
'Host':'guba.eastmoney.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',

    }

        # self.proxies = get_ip()
    products = [
        # '中信保诚、光大保德信、国海富兰克林'
                ['type,zg80065113','中欧'],
        #         ['type,zg80168726','平安'],
        #         ['type,zg80000226','博时'],
        #         ['type,zg80145102','东证资管'],
        #         ['type,zg80000243','长信'],
        #         ['type,zg80036782','招商'],
        #         ['type,zg80000249','新华'],
        #         ['type,zg80000230','鹏华'],
        #         ['type,zg80075936','中邮'],
        #         ['type,zg80128562','富安达'],
        #         ['type,zg80000223','嘉实'],
        #         ['type,zg80000221','富国'],
        #         ['type,zg80036742','兴全'],
        #         ['type,zg80050229','上投摩根'],
        #         ['type,zg80092233','农银汇理'],
        #         ['type,zg80000228','华安'],
        #         ['type,zg80065990','建信'],
        #         ['type,zg80000248','广发'],
        #         ['type,zg80000220','南方'],
        #         ['type,zg80041198','天弘'],
        #         ['type,zg80053708','汇添富'],
        #         ['type,zg80000222','华夏'],
        #         ['type,zg80036782','招商'],
        #         ['type,zg80000229','易方达'],
        #         ['type,zg80044515','国海富兰克林'],
        #         ['type,zg80066470','中信保诚'],
        #         ['type,zg80036797','摩根士丹利华鑫'],
        #         ['type,zg80048088','光大保德'],
        #         ['type,zg80064562','交银'],
                # ['type,zg80055334','华泰柏瑞'],
                # ['type,zg80000235','银华'],
                # ['type,zg80053204', '华商'],
        # 'list,of162411',     # 华宝标普油气上游股票人民币A吧

        ]
   
    def start_requests(self):

        for product,name in self.products:
            # product = product.replace('list','type')
            max_test = 1
            start_url = f"http://guba.eastmoney.com/{product}_1.html"
            print(start_url,1111111111111111111111111)
            yield scrapy.Request(start_url,headers= self.header ,callback=self.parse,
                meta = {'product':product,'max_page':max_test,'jj_name':name})

    def parse(self, response):

        max_test = response.meta['max_page']
        product = response.meta['product']
        jj_name = response.meta['jj_name']
        nick_name = response.xpath('//*[@id="stockname"]//text()').get()
        data_list = response.xpath("//div[@id='articlelistnew']/div[contains(@class,'articleh')]")
        for info in data_list:
            tags = info.xpath("./span[@class='l3']")
            em = tags.xpath('./em/text()').get()

            if any(i == em for i in ['公告','讨论']):
                continue
            content = tags.xpath("./a/@title").get()
            cotent_url = response.urljoin(tags.xpath("./a/@href").get())
            
            #http://guba.eastmoney.com/list,of004549_1.html
            media = info.xpath("./span[@class='l4']/a/text()").get()
            time_ = info.xpath("./span[@class = 'l5']/text()").get()
         
            other_time = time.strptime(time_,'%m-%d %H:%M')
            other_time_ = '2021'+time.strftime('%m-%d',other_time)
            #时间判断页数的
            other_time_tuple = '2021' + time.strftime('%m%d', other_time)
            data = PaperItem(title = content,url = cotent_url,date = other_time_tuple
            ,media = nick_name,content = content+nick_name,jj_name=jj_name,media_orig = nick_name,reporter = media,
            post_type = 1)
            # if old_urls_from_jijin_urls(cotent_url):
            #     logger.info(f"{cotent_url} already exist")
            #     continue
            yield scrapy.Request(cotent_url,callback=self.parse2,meta={'data':data},dont_filter=True)
        # if '04-' in other_time_tuple:

        if all(i not in other_time_  for i in ['08-','09-','10-','11-','12-']):
            if other_time_.replace('-','') >='20210525':

                # next_page = response.xpath("//span[@class='pagernums']/span/a[contains(text(),'下一页')]/@href").get()
                # print(response.url,next_page,2222)
                # nex_url = response.urljoin(next_page)
                max_test+=1

                nex_url = response.urljoin(f"{product}_{max_test}.html")
                print(nex_url,123123)
                # logger.info(nex_url, retention="10 days")
                yield scrapy.Request(nex_url,callback=self.parse,meta={'product':product,'max_page':max_test,'jj_name':jj_name},dont_filter=True)

    def parse2(self,response):

        media_ori = response.xpath("//span[@id ='stockif']/span/a/text()").get()
        data = response.meta['data']
        data['media_orig'] = media_ori
        data['media'] = media_ori
        print(data)
        yield data

