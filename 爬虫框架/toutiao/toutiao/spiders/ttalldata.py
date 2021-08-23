# -*- coding: utf-8 -*-
import json
import re

import requests
from scrapy import Request
import pymysql
import scrapy
from redis import Redis
from scrapy.loader.processors import MapCompose, SelectJmes
from scrapy.utils.project import get_project_settings
from pyquery import PyQuery as pq
import re
from ..items import SpiderRedisItem

class TtalldataSpider(scrapy.Spider):
    name = 'ttalldata'
    allowed_domains = ['tsearch-hl.snssdk.com']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {

            'User-Agent': 'com.ss.android.article.news/7552 (Linux; U; Android 6.0; zh_CN; Coolpad 8737; Build/MRA58K; Cronet/TTNetVersion:3e14bd94 2019-12-05)'
        },
        'DOWNLOADER_MIDDLEWARES': {

            'toutiao.middlewares.RandomProxy': 600,
        },
        'ITEM_PIPELINES': {
            'toutiao.pipelines.ToutiaoPipeline': 200,
            'scrapy_redis.pipelines.RedisPipeline': 300

        }}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.redis = Redis(host="tz6.zhangyupai.net", password="zz121212", port=6379, db=0)
        self.cookies = get_project_settings().get("COOKIES_TT_IPHONE")

    def start_requests(self):
            for i in range(0,20):
                page = i*10
                # url = f'https://m.toutiao.com/search/?keyword=%E5%98%89%E5%AE%9E%E5%9F%BA%E9%87%91&pd=information&source=search_subtab_switch&traffic_source=&original_source=&in_tfs=&in_ogs=&format=json&count=10&offset={page}&from=news&search_id=2020071321591201001002919417695B35&start_index={page}&index_resource=&filter_vendor=&filter_period=&min_time=&max_time=&from_search_id='
                url = f'https://is-lq.snssdk.com/search/?keyword=嘉实基金&from=news&loadId=1&keyword_type=hist&cur_tab_title=search_tab&pd=information&source=search_subtab_switch&search_position=search_bar&action_type=history_keyword_search&search_start_time=1594689992067&plugin_enable=3&iid=2559313051662279&device_id=49435920583&ac=wifi&mac_address=54%3ADC%3A1D%3AA8%3AF5%3A24&channel=360_2&aid=13&app_name=news_article&version_code=755&version_name=7.5.5&device_platform=android&ab_version=668779%2C660830%2C662176%2C1843682%2C1403339%2C662099%2C668774%2C1852639%2C1419049%2C1809701%2C1847468%2C668775%2C1157750%2C1789127%2C1469498%2C1812121%2C1484967%2C1855226%2C1419597%2C1789133%2C1529251%2C1851966&ab_group=94566%2C102755&ab_feature=102755%2C94566&device_type=Coolpad+8737&device_brand=Coolpad&language=zh&os_api=23&os_version=6.0&uuid=863277031456940&openudid=29ef196b33604ffa&manifest_version_code=7552&resolution=720*1184&dpi=320&update_version_code=75517&_rticket=1594689979452&plugin=18762&tma_jssdk_version=1.46.0.13&pos=5r_-9Onkv6e_eSULeic3eDk6dBwOv7G_8fLz-vTp6Pn4v6esr6yzqKypr6qpsb_x_On06ej5-L-nrqyzr66pqK6lsb_88Pzt3vTp5L-nv3klC3onN3g5OnQcDr-xv_zw_O3R8vP69Ono-fi_p6yvrLOorKmvqqmxv_zw_O3R_On06ej5-L-nrqyzr66pqK6l4A%3D%3D&rom_version=23&cdid=833ac823-8313-46c3-8a58-f9167a074c4b&is_ttwebview=1&fetch_by_ttnet=1&latitude=31.234538&longitude=121.514274&search_sug=1&forum=1&from_pd=synthesis&index_resource=&min_time=&max_time=&format=json&count=10&offset={page}&filter_vendor=&filter_period=&from_search_id='
                '''手机端全部数据接口'''
                # url = f'''https://is-lq.snssdk.com/search/?search_id=&from_search_subtab=&source=input&has_count=&offset={page}&is_ttwebview=1&count=10&action_type=input_keyword_search&keyword_type=&from=weitoutiao&search_position=search_bar&format=json&is_from_native=1&keyword=嘉实基金&pd=weitoutiao&search_load_id=1&qc_query=&iid=2559313051662279&device_id=49435920583&ac=wifi&mac_address=54%3ADC%3A1D%3AA8%3AF5%3A24&channel=360_2&aid=13&app_name=news_article&version_code=755&version_name=7.5.5&device_platform=android&ab_version=1403339%2C662099%2C1843682%2C1852639%2C668774%2C1484967%2C1789133%2C1469498%2C1789127%2C1419597%2C1157750%2C1419049%2C1855226%2C1812121%2C1529251%2C668775%2C1847468%2C1809701%2C668779%2C660830%2C662176%2C1859936%2C1851966&ab_group=94566%2C102755&ab_feature=102755%2C94566&ssmix=a&device_type=Coolpad+8737&device_brand=Coolpad&language=zh&os_api=23&os_version=6.0&uuid=863277031456940&openudid=29ef196b33604ffa&manifest_version_code=7552&resolution=720*1184&dpi=320&update_version_code=75517&_rticket=1594692546962&plugin=18762&tma_jssdk_version=1.46.0.13&pos=5r_-9Onkv6e_ez0LdAEDdSoyv7G_8fLz-vTp6Pn4v6esr6yzqKypr6Slsb_x_On06ej5-L-nrqyzr66pq7G__PD87d706eS_p797PQt0AQN1KjK_sb_88Pzt0fLz-vTp6Pn4v6esr6yzqKypr6Slsb_88Pzt0fzp9Ono-fi_p66ss6-uqavg&rom_version=23&cdid=833ac823-8313-46c3-8a58-f9167a074c4b'''
                '''微头条网址'''
                print(url)

                yield scrapy.Request(url, callback=self.parse_2,dont_filter=True)

    def parse_2(self,response):


        Filter_data = MapCompose(json.loads, SelectJmes('dom'))
        ll_Data_List = Filter_data(response.text)


        str_data =  str(ll_Data_List[0])

        doc = pq(str_data)

        data_list = doc("div.result-content")

        for info in data_list.items():

            # media = info("div.ttfe-flex-item.ts-size14").text()
            # media_link = info('div.ttfe-flex.ttfe-flex-align-center a').attr('href')
            # media_link_id = re.search(r'fw_user_id=(.*?)&',media_link).group(1)
            # Data_ = SpiderRedisItem(media_orig=media,media_id = media_link_id)
            data_ = info.attr('cr-params')
            data_json = json.loads(data_)

            gid = data_json.get('gid')
        #
            toutiao_url= f'https://www.toutiao.com/a{gid}'
            self.redis.lpush('TTurl:start_urls', toutiao_url)
            print(toutiao_url)
            # resp = requests.post(toutiao_url).text
            # media_id = re.search(r"uid: '(.*?)',", resp).group(1)
            # media = re.search(r"name: '(.*?)',", resp).group(1)
            # Data_ = SpiderRedisItem(media_orig=media, media_id=media_id)
            # yield Data_
            # print(resp)
            # yield scrapy.Request(toutiao_url,method='POST',callback=self.parse3,dont_filter=True)
            # yield Data_

    # def parse3(self, response):
    #     print(response.text)
    #     url = response.url
    #     if 'i' in url:
    #
    #         media_id = re.search(r"uid: '(.*?)',",response.text).group(1)
    #     else:
    #         media_id = re.search(r"userId: (.*?),", response.text).group(1)
    #     media = re.search(r"name: '(.*?)',", response.text).group(1)
    #     Data_ = SpiderRedisItem(media_orig=media,media_id = media_id)
    #     print(media_id,media,222222222)
    #     yield Data_


