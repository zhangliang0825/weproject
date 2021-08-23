
import csv
import datetime
import re
from pyquery import PyQuery as pq
import pymysql
import redis
from loguru import logger
dbhost3 = '120.26.106.222'
dbuser3 = 'julai01'
passwd3 = 'Sh51785136@sh'
dbname3 = 'jijin'
logger.add('log_text.log')
dbhost = '120.26.211.213'
dbuser = 'julai01'
passwd = 'Zycj@2020688'
dbname = 'news_caiji'
conn = pymysql.connect(dbhost, dbuser, passwd, dbname, charset='utf8')
cur = conn.cursor()
media_sql = 'SELECT distinct b.id,b.title,a.media_channel FROM hisinfo_cx a INNER JOIN cx0308 b ON a.`post_id` = b.`id` WHERE a.post_type = 3 AND a.str_date >= 20210628 and a.grp_id = 0'
conn3 = pymysql.connect(dbhost3, dbuser3, passwd3, dbname3, charset='utf8')
cur3 = conn3.cursor()
cur3.execute(media_sql)
all_dict = {}

all_media_list = cur3.fetchall()

sql = f'''select distinct post_id,media from hisinfo_cx where media_union = '' and del_flag = 0 and str_date >20210620 and post_type not in (1,5,10,15,7)'''
cur3.execute(sql)
data_list = cur3.fetchall()
for id_,media in data_list:
    media = media.encode("gbk", 'ignore').decode("gbk", "ignore").strip('[').strip(']').strip("{").strip("}")
    print(media)
    a = [media_name for media_name, media_list in all_media_list if
         media in [i for i in media_list.split("|") if i != '']]

    if a:
        media_union = a[0]
    else:
        media_union = media
    sql = 'update hisinfo_cx set media_union = %s  where post_id = %s '
    cur3.execute(sql, (media_union, id_))
    conn3.commit()
    sql = 'update news2019_dyn set media_union = %s where post_id = %s '
    cur3.execute(sql, (media_union, id_))
    conn3.commit()
    print(111111111111111, media_union, sql, id_)