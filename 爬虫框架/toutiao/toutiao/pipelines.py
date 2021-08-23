# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import requests
from scrapy.utils.project import get_project_settings


class ToutiaoPipeline:

    def __init__(self):

        self.insert_url = 'http://tz4.zhangyupai.net:81/mobile/import_news1.php'
    #
    # def open_spider(self,spider):
    #     get_setting = get_project_settings()
    #     self.db_config = get_setting.get("DB_CONFIG")
    #     self.db = pymysql.connect(self.host, self.user,
    #         self.password, self.database, charset='utf8')
    #     self.cursor = self.db.cursor()
    #
    #
    #
    # def close_spider(self,spider):
    #     self.cursor.close()

    def process_item(self, item, spider):

        # sql = 'select media from media'
        # self.cursor.execute(sql)
        # self.all_data = [i[0] for i in self.cursor.fetchall()]
        # media = item.get("media_orig")
        # if media not in self.all_data:
        #     media_id = item.get("media_id")
        #     media_orig = item.get("media_orig")
        #     sql = 'insert into media(media,link) values (%s,%s)'
        #     self.cursor.execute(sql,(media_orig,media_id))
        #     self.db.commit()
        if spider.name == 'shipin':

            item.update({'post_type':20})
            for i in range(1, 10):

                print(i, '页数...')
                try:

                    res = requests.post(self.insert_url, data=item, timeout=12).text
                    print(res)
                    if '1' in str(res):
                        break
                    return '成功'
                except Exception as e:
                    print(e)
            print(222222222222222222011111111114444)

        return item
