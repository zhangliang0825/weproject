# -*- coding: utf-8 -*-
import copy
import hashlib
import threading
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
import time
from twisted.enterprise import adbapi

import pymysql
from collections import OrderedDict
import datetime

from .tools import getLoger
# from loguru import logger

# logger.add('头条日志实时采集url.log',retention='3 days')
# to_now = datetime.now()
# to_day = to_now.strftime('%Y%m%d')
today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = str(today-oneday)


class SpiderRedisPipeline(object):
    def __init__(self,db_pool):
        self.db_pool = db_pool
        self.data = {'title': '', 'content': '', 'post_type': '', 'summary': '', 'media_orig': '',
                                 'reporter': '', 'content_url': '', 'str_date': '', 'username': '', 'is_orig': 1,
                                 'meta_info': '', 'spider': 'tth_m','bizname': '',
                     'biz': '',}
        # self.insert_url = 'http://tz4.zhangyupai.net:81/mobile/import_mynews1.php'
        #
        self.sql = None
        # self.post_url = 'http://tz4.zhangyupai.net:81/mobile/import_ttnews1.php'
        # self.weixin_url =  'http://tz4.zhangyupai.net:81/mobile/import_wxpost.php'
        self.lock = threading.RLock()
        self.mylog = getLoger('数据日志' + '.log')

    @classmethod
    def from_settings(cls, settings):
        # 用一个db_params接收连接数据库的参数
        db_params = dict(
            host=settings.get('MYSQL_HOST2'),
            database=settings.get('MYSQL_DATABASE3'),
            user=settings.get('MYSQL_USER2'),
            password=settings.get('MYSQL_PASSWORD2'),
            charset='utf8',


            # use_unicode=True,
            # 设置游标类型
            cursorclass=pymysql.cursors.DictCursor
           
        )
        db_pool = adbapi.ConnectionPool('pymysql', **db_params,   cp_reconnect=True)

        # 创建一个链接池
        return cls(db_pool)

    @property
    def sql_is(self):
        if not self.sql:
            self.sql = '''insert into data(biz,title,text,html,link,media,datetime,media_id,type)values(%s,%s,"%s",%s,%s,%s,%s,%s,%s)'''
            return self.sql
        return self.sql

    def multiple_replace(self,text, idict):
        if idict == {}:
            return text
        else:
            rx = re.compile('|'.join(map(re.escape, idict)))

            def one_xlat(match):
                return idict[match.group(0)]

        return rx.sub(one_xlat, text)

    def process_item(self, item, spider):
        content = item['content']
        dict_ = {r'\u003E': '>', r'\u003C\u002F': '</', '&quot;': '', r'\u003C': '<'}
        content = self.multiple_replace(content, dict_)
        title = item['title']
        content_url = item['content_url']
        if 'toutiao' in content_url:
            if '/w/' in content_url:
                title = re.sub(r'\s+', '', title)
                if any(i in title for i in ['?',"!",'？','！','！ ']) and '。' in title:
                    gap_word1 = [i.span() for i in re.finditer('？|\?|！|!|？|！ ', title)][0][0]
                    gap_word2 = [i.span() for i in re.finditer('。', title)][0][0]

                    if gap_word1<=gap_word2:
                        titles = re.split("？|\?|！|!|！ ", title)[0]
                    else:

                        gap_word1 = [i.span() for i in re.finditer('，|， |，|,', title)][1][0]

                        gap_word2 = [i.span() for i in re.finditer('。', title)][0][0]
                        if gap_word1 < gap_word2:

                            titles = ','.join(re.split("，|， |，|,", title)[:2])
                        else:
                            titles = re.split('。', title)[0]
                elif any(i in title for i in ['，', ",", '， ']) and not any(i in title for i in ['?',"!",'？','！','！ '])\
                        and '。' in title:

                    gap_word1 = [i.span() for i in re.finditer('，|， |，|,', title)][0][0]

                    gap_word2 = [i.span() for i in re.finditer('。', title)][0][0]
                    if gap_word1<gap_word2:

                        titles = ','.join(re.split("，|， |，|,",title)[:2])
                    else:
                        titles = re.split('。',title)[0]


                else:

                    if '。' not in title:
                        title = re.split(',|，',title)[:2]
                        titles = '，'.join(title)
                    else:
                        titles = re.split('。',title)[0]


            else:
                    # title = ''.join(re.findall(r'[^\x00-\xff]|[0-9]{5}', title))
                if '。' in title and '】' not in title:
                    titles = title.replace('&quot;', '').split('。')[0]
                # elif '】' in title:
                #     titles = title.replace('&quot;', '').split('】')[0] + "】"
                else:
                    titles = title.replace('&quot;', '')
        else:
            titles = title

        item['content'] = content+item['media_orig']

        item['title'] = titles
        with self.lock:
            defer = self.db_pool.runInteraction(self.insert_data,item,spider)
            defer.addErrback(self.handle_error,item, spider)
        return item


    def insert_data(self,cursor, item,spider):
            content = item['content']
            url = item['content_url']
            
            str_date = item['str_date']
            if spider.name == 'toutiao':
                if 'com/w/' in url:
                    self.data.update({'post_type': 17})
                else:
                    self.data.update({'post_type': 6})
                time_str = datetime.datetime.strptime(str(str_date.replace(' ', '')), '%Y-%m-%d%H:%M:%S')
                time_time = time.mktime(time_str.timetuple())
                rukudate = time.strftime('%Y%m%d', time.localtime(time_time))
            elif spider.name == 'souhu':
                self.data.update({'post_type': 14})
                time_s = time.strptime(str_date, '%Y-%m-%d %H:%M')
                time_s = time.strftime('%Y%m%d', time_s)
                rukudate = time_s
            elif spider.name == 'weibo':
                self.data.update({'post_type': 7})
                self.data.update({'spider': '微博'})
                rukudate = item['str_date']
            else:
                self.data.update({'post_type': 3})
                self.data.update({'spider': '搜狗'})
                rukudate = item['str_date']
            self.data.update(item)
            self.data.update({'str_date':rukudate})

            if rukudate >=yesterday.replace('-',''):

                self.mylog.info((url,content[:60]))

                content_text = item['content']
                content = str(bytes(content_text, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
                content_split = [str(bytes(i, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk')) for
                                 i in content.split('。')]
                content_p = (''.join(content_split[i:i + 3]) for i in range(0, len(content_split), 3))
                media = item['media_orig']
                if media != '金融界':
                    if spider.name == 'toutiao':
                        cursor.execute(self.sql_is,('', item.get("title"), tuple(content_p), content, item.get("content_url"), item.get("media_orig"), str_date,  item.get("media_orig"), "头条"))
                    elif spider.name == 'sougou':
                        sign = hashlib.md5(item.get("content_url").replace('http://','').encode('utf-8')).hexdigest()
                        html_text =  item.get("html")
                        html = str(bytes(html_text, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
                        cursor.execute(self.sql_is, (
                            sign, item.get("title"), tuple(content_p),html, item.get("content_url"),
                            item.get("username"), str_date, item.get("media_orig"), "搜狗"))
                    elif spider.name == 'weibo':
                        cursor.execute(self.sql_is, (
                            '', item.get("title"), content_text, '', item.get("content_url"),
                            item.get("username"), str_date, item.get("media_orig"), "微博"))

                    else:
                        cursor.execute(self.sql_is, (
                        '', item.get("title"), tuple(content_p), content, item.get("content_url"),
                        item.get("media_orig"), str_date, item.get("media_orig"), "搜狐"))

                    return item

    def handle_error(self,error, item,spider):
        print('error',error)