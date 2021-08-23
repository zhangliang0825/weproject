import re

import pymysql

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
media_sql = 'SELECT DISTINCT b.id,b.title ,a.media_channel,a.post_type FROM hisinfo_cx a INNER JOIN cx0308 b ON a.`post_id` = b.`id` WHERE a.post_type IN (3) AND a.str_date >= 20210812 AND a.del_flag = 0'
conn3 = pymysql.connect(dbhost3, dbuser3, passwd3, dbname3, charset='utf8')
cur3 = conn3.cursor()
cur3.execute(media_sql)
all_dict = {}
for item in cur3.fetchall():
    title = ''.join(re.findall(u'[\u4e00-\u9fa5]', item[1]))
    item = list(item)
    item[1] = title
    item = tuple(item)
    all_dict.setdefault((item[1:]),[]).append(item[0])
for key, value in all_dict.items():
    media = key[1]
    id_max = [i for i in value if i != min(value) ]
    print(key,id_max)
    if id_max == []:
        continue
    if len(id_max) == 1:
        id_max = str(tuple(id_max)).replace(",", "")
    else:
        id_max = tuple(id_max)
    sql = f'update hisinfo_cx set del_flag =1 where post_id in {id_max}'
    print(sql)
    cur3.execute(sql)
    conn3.commit()
    print(sql,11)


