import re
import time

import pymysql
import scrapy
from redis import Redis


from lxml import etree
from scrapy.utils.project import get_project_settings
from ..tools import getLoger
import datetime
from scrapy_redis.spiders import RedisSpider



class DataInsertSpider(RedisSpider):
    name = 'insert_2_data'
    allowed_domains = ['zhangyupai.net']
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'content-type': "application/json"
        },
        'CONCURRENT_REQUESTS' : 1,
        'DOWNLOAD_DELAY': 0.6,
        'DOWNLOAD_TIMEOUT': 10,
        'REDIS_URL' : 'redis://root:Lz@12@12@julai@tz6.zhangyupai.net:6379/9'

    }
    redis_key = 'ID_numss:start'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        get_setting = get_project_settings()


        self.cookies = get_setting.get("COOKIES_TT")



        self.host = get_setting.get("MYSQL_HOST2")
        self.user = get_setting.get("MYSQL_USER2")
        self.password = get_setting.get("MYSQL_PASSWORD2")
        self.database = get_setting.get("MYSQL_DATABASE3")


        self.data_set = set()
        self.souhu_url = 'http://tz4.zhangyupai.net:81/mobile/import_mynews1.php'
        self.tt_url = 'http://tz4.zhangyupai.net:81/mobile/import_ttnews1.php'
        self.wx_url = 'http://tz4.zhangyupai.net:81/mobile/import_wxpost.php'
        self.mylog = getLoger(self.name + '.log')

    def make_request_from_data(self, data):
        print(data,11111111111)
        return self.make_requests_from_url(data)

    def make_requests_from_url(self, data):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()
        sql = f'select id,title,text,html,link,media,datetime,media_id,type from data where id={data.decode("utf-8")} and type not in ("微信")'
        print(sql)
        self.cursor.execute(sql)

        all_data_list = self.cursor.fetchone()

        if all_data_list:
            id_, title, text, html, link, media, datetime_, media_id, type_ = all_data_list
            print(id_, title )


            if '-' in datetime_:
                datetime_ = ''.join(re.split(r'-|\s+', datetime_)[:3])

            else:
                datetime_ = datetime_
            if 'com/i' in link:
                type_num = 6
                url = self.tt_url
            elif 'com/w/' in link:
                type_num = 17
                url = self.tt_url
            elif type_ == '搜狐':

                type_num = 14
                url = self.souhu_url
            elif type_ == '搜狗':
                response = etree.HTML(html)
                html = ''.join(response.xpath("//div[@class='rich_media_content ']//text()"))
                html = re.sub('\s+', '', html)
                sougou_url_pattern = link.replace("http://mp.weixin.qq.com/s?", "")
                new_url_pattern = f'http://xc.zhangyupai.net:8181/weixintest/weixin_id/{id_}/'
                link = new_url_pattern + sougou_url_pattern + f'&{media}'
                type_num = 3
                url = self.wx_url
            elif type_ == '微博':
                type_num = 7
                html = text
                url = self.souhu_url
            if '信息披露' not in title:
                datas = {'title': title, 'content': html, 'post_type': str(type_num), 'summary': html[:60],
                         'media_orig': '',
                         'reporter': '', 'content_url': link, 'str_date': datetime_, 'username': type_,
                         'is_orig': '1',
                         'meta_info': '', 'spider': type_, 'bizname': '',
                         'biz': '', }
                if type_num == 3:
                    datas.update({'media_orig': media_id, 'bizname': media, 'biz': str(id_), })
                elif type_num == 7:
                    datas.update({'media_orig': media, 'media_channel': '微博'})
                elif type_num == 14:
                    datas.update({'media_orig': media, 'media_channel': '搜狐'})
                else:
                    datas.update({'media_orig': media})
                return scrapy.FormRequest(url, formdata=datas, callback=self.parse, meta={
                    'id_': id_
                }, dont_filter=True)
        self.cursor.close()

    def parse(self, response):
        print(response.text)