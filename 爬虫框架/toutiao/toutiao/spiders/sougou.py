# -*- coding: utf-8 -*-
import csv
from datetime import datetime,timedelta
import re
from ..tools import getLoger
import time
import os
import pymysql
import requests
import scrapy
from redis import Redis
from scrapy.utils.project import get_project_settings
from loguru import logger
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
yesterday = datetime.today()+timedelta(-1)

yesterday = yesterday.strftime('%Y%m%d')
class SougouSpider(scrapy.Spider):
    new_time = time.time()
    now_day = time.strftime('%Y-%m-%d%H:%M:%S', time.localtime(time.time()))
    name = 'sougou'
    allowed_domains = ['weixin.sogou.com']

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'Cookie': '__utmz=24953151.1592959631.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PIXIEL_RATIO=1.5; sso_auth_status=ff666bef2638d04593de6c1619a008f0; sso_uid_tt=3aab2c0d7e6b017b0ea25f2dc09e7ec4; sso_uid_tt_ss=3aab2c0d7e6b017b0ea25f2dc09e7ec4; toutiao_sso_user=6b202cdd3c7266fdee4250dd777c6c58; toutiao_sso_user_ss=6b202cdd3c7266fdee4250dd777c6c58; passport_auth_status=374941f129ff88fee478dbf9632801be%2Cd6cbe685fe989c938d5cbfd3c56dc9ea; sid_guard=6d59bafe68b1d4985bbafd8acc5f815a%7C1594191164%7C5184000%7CSun%2C+06-Sep-2020+06%3A52%3A44+GMT; uid_tt=36eb4fca4ae8694c71028232f426bf92; uid_tt_ss=36eb4fca4ae8694c71028232f426bf92; sid_tt=6d59bafe68b1d4985bbafd8acc5f815a; sessionid=6d59bafe68b1d4985bbafd8acc5f815a; sessionid_ss=6d59bafe68b1d4985bbafd8acc5f815a; tt_webid=6846998871970448904; __utma=24953151.710770063.1592959631.1592959631.1594278577.2; SLARDAR_WEB_ID=6846998871970448904; RT="z=1&dm=toutiao.com&si=fnn5vftq4q7&ss=kcfz3q4v&sl=1&tt=0&obo=1&ld=3bnp20&r=bbe4ce7ddc46c6df117239442a065abc&ul=3bnp25&hd=3bnp2l"; WIN_WH=1280_578; tt_webid=6843736986450331143',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }, 'DOWNLOAD_DELAY':1.5,
        'DOWNLOADER_MIDDLEWARES':{
            'toutiao.middlewares.RandomProxy':501
        }


    }

    def __init__(self, **kwargs):


        get_setting = get_project_settings()
        self.host = get_setting.get("MYSQL_HOST3")
        self.user = get_setting.get("MYSQL_USER3")
        self.password = get_setting.get("MYSQL_PASSWORD3")
        self.database = get_setting.get("MYSQL_DATABASE5")
        self.db = pymysql.connect(self.host, self.user,
        self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()

        self.redis = Redis(host="tz6.zhangyupai.net", password="Lz@12@12@12@", port=6379, db=8)
        self.mylog = getLoger(self.name + '.log')
        sql = 'SELECT title,media FROM data WHERE id >2521915 AND type = "搜狗"'
        self.cursor.execute(sql)
        self.data_list_crawler = [[''.join(re.findall(r'[\u4E00-\u9FA50-9]+',title))[:18], media] for title, media in self.cursor.fetchall()]
        conn = pymysql.connect(host='120.26.211.213', user='julai01', password='Zycj@2020688', database='news_caiji',
            charset='utf8mb4', )
        sql = '''select name from weixin where type =1'''

        with conn.cursor() as cur:
            cur.execute(sql)
            all_data_exclude = [i[0] for i in cur.fetchall()]

        with open(r'微信实时列表.csv', 'r', encoding='utf8', newline='') as f:
            writer = list(csv.reader(f))
            name_list = sum(writer, [])

        self.all_media_data_list = all_data_exclude + name_list

    def get_new_cookies(self
                        ):
        # 搜狗视频url
        url = 'https://v.sogou.com/'

        rst = requests.get(url=url,
            headers=headers,
            allow_redirects=False,
        )
        cookies = rst.cookies.get_dict()

        return cookies



    def start_requests(self):
        jijin_list = ('华安','泓德', '汇安', '国海富兰克林', '景顺长城', '嘉实', '中银', '中邮', '长信', '富安达', '富国', '华夏', '南方', '国寿安保',
                      '天弘', '博时', '易方达', '鹏华', '新华', '银华', '交银', '大成', '汇丰晋信', '中信保诚', '博时', '建信', '华宝',
                      '招商', '广发', '上投摩根', '中融', '工银瑞信', '华泰柏瑞', '中欧', '前海开源', '汇添富', '东证资管', '兴全',
                      '华商', '国泰',  '平安', '农银汇理', '海富通', '光大保德信', '摩根士丹利华鑫', '华商', '民生加银')
        for name in jijin_list:
            if len(name) > 3:
                name = name
            else:
                name = name + '基金'
            # for i in range(1, 11):

            url = f'https://weixin.sogou.com/weixin?query={name}&_sug_type_=&tro=on&sut=3508&lkt=1%2C1616389972077%2C1616389972077&s_from=input&_sug_=y&type=2&sst0=1616389972181&page=1&ie=utf8&w=01019900&dr=1'

            yield scrapy.Request(url,callback=self.parse,cookies=self.get_new_cookies(),
                dont_filter=True)



    def parse(self, response):
        all_data_str = []
        yesterday = datetime.today() + timedelta(-1)

        yesterday_str = yesterday.strftime('%Y%m%d')
        content_list = response.xpath("//ul[@class='news-list']/li")
        for info in content_list:

            re_time = info.xpath(".//span[@class='s2']/script/text()").get()

            re_time_int = re.findall(r'\d+', str(re_time))[0]

            Other_time = time.localtime(int(re_time_int))
            post_time_s = time.strftime('%Y%m%d', Other_time)
            title_ = ''.join(info.xpath('.//h3/a//text()').getall()).strip()
            title = ''.join(re.findall(r'[\u4E00-\u9FA50-9]+',title_))[:18]
            meida = info.xpath('.//div[@class="s-p"]/a/text()').get().strip()
            all_data_str.append(post_time_s)
            print(title,meida,post_time_s)
            if [title,meida] not in self.data_list_crawler \
                    and post_time_s >=yesterday_str and meida not in self.all_media_data_list:

                link = 'https://weixin.sogou.com' + info.xpath(".//h3/a/@href").get()


                yield  scrapy.Request(link,callback=self.get_link,cookies=self.get_new_cookies(),
                meta={'title':[title,meida]})

        next_page = response.xpath("//div[@class = 'p-fy']/a[text()='下一页']")
        max_str_date = max(all_data_str)
        print('最大的时间',max_str_date,yesterday_str)

        if next_page and max_str_date >= yesterday_str:
            next_url_text = response.xpath("//div[@class = 'p-fy']/a[text()='下一页']/@href").get()

            next_url = response.urljoin(next_url_text)
            print(next_url,'下一页...................')
            yield scrapy.Request(next_url,callback=self.parse,cookies=self.get_new_cookies(),
                dont_filter=True)

    def get_link(self,response):
        title,meida = response.meta['title']
        index_url = ''.join(re.findall(r"url \+= '(.*?)';", response.text))
        self.redis.lpush('SGurl:start_urls', index_url)
        self.data_list_crawler.append([title,meida])
        self.mylog.info((media,index_url))
