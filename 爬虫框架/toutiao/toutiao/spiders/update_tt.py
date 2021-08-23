import json
import os
import re
import time
import pymysql
import scrapy
from redis import Redis
from scrapy.utils.project import get_project_settings



class TtSpider(scrapy.Spider):
    # logger.add('tt数据记录.log', retention='1 days')
    name = 'update_tt'
    allowed_domains = ['toutiao.com']

    custom_settings = {
       'DOWNLOAD_TIMEOUT':10,
    'REDIRECT_ENABLED': False,

        'DOWNLOADER_MIDDLEWARES': {
            'toutiao.middlewares.UserAgentDownloadMiddleware': 500,
            # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
            # 'toutiao.middlewares.RandomProxy': 600,
        },
    }


    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        get_setting = get_project_settings()
        self.cookies = get_setting.get("COOKIES_TT_UPDATE")

        self.redis = Redis.from_url(get_setting.get("REDIS_URL"))

        self.db_config = get_setting.get("DB_CONFIG")

    def read_js(self,media):
        path2 = os.path.abspath('..')
        url = f'https://www.toutiao.com/toutiao/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword={media}&autoload=true&count=20&enqc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1615710857498'
        resp = os.popen('node {} "{}"'.format(path2 + r'/toutiao/toutiao/js/sigin.js',url))
        sigin = resp.read().strip()
        index_url = f'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword={media}&autoload=true&count=20&en_qc=1&cur_tab=4&from=media&pd=user&timestamp=1615877594666&_signature={sigin}'


        return index_url



    def start_requests(self):
        self.db = pymysql.connect(**self.db_config)
        self.cursor = self.db.cursor()#创建游标
        sql = '''SELECT media,link,token FROM media WHERE post_type IN (1) AND link <>  "" and id >32584 '''
        # sql = '''SELECT media,link,token FROM media WHERE post_type IN (1) AND link =  "" or link = null'''
        self.cursor.execute(sql)
        all_data_list = self.cursor.fetchall()
        for meida, media_id, token in all_data_list:

            if media_id !='':
                user_url = 'https://www.toutiao.com/c/user/{}/'.format(media_id.strip())
            else:
                user_url = self.read_js(meida)
            print(user_url)
            yield scrapy.Request(user_url, callback=self.parse,cookies=self.cookies,meta={'dont_redirect': True,
                                                                     'media_id':media_id,
                                                                     'media':meida

            },
                dont_filter=True)



    def parse(self, response):

        media = response.meta['media']
        data_json = json.loads(response.text)
        data_list = data_json.get("data")
        print(data_list)
        if data_list:
            keyword = [i.get("id") for i in data_list if i.get("name") ==media.strip()]
            if keyword:
                print(keyword)
                sql = 'update media set link = %s where media =%s'

                self.cursor.execute(sql,(keyword[0],media))
                self.db.commit()
                print(sql,keyword)
            else:
                sql = 'delete from media where media = %s'
                self.cursor.execute(sql,(media))
                self.db.commit()
                print(media,'删除......')

        ####################################################
        #
        # media_id = response.meta['media_id']
        # media = response.meta['media']
        # user_code = response.headers.getlist('Location')
        #
        # user_code = user_code[0].decode('utf-8')
        # print(user_code,media_id,media)
        # if '404_not_found' not in user_code:
        #     token = re.findall(r'token/(.*?)/', user_code)[0]
        #     sql = 'update media set token = %s where link = %s'
        #     self.cursor.execute(sql,(token,media_id))
        #     self.db.commit()
        #     print(token,media_id)
        # elif '404_not_found'  in user_code:
        #     sql = 'delete from media where link = %s'
        #     self.cursor.execute(sql,(media_id))
        #     self.db.commit()
        #     print(media_id,'删除..................')
        #

