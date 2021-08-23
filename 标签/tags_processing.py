# from Semantic_processing import get_content


import csv

import pymysql

dbhost = '120.26.106.222'
dbuser = 'julai01'
passwd = 'Sh51785136@sh'
dbname = 'jijin'

conn = pymysql.connect(dbhost, dbuser, passwd, dbname, charset='utf8')
cur = conn.cursor()

sql = "SELECT  a.`post_id`,b.`media`  FROM news2019_dyn a INNER JOIN news2019 b ON  a.`post_id` = b.`post_id` WHERE a.topic <> '' AND b.`str_date` >=20190901 ORDER BY b.`str_date` ASC"


cur.execute(sql)

data_list = cur.fetchall()

file_csv = csv.reader(open('统计媒体.csv','r',encoding='utf-8'))
all_media_list  = [i for i in file_csv]

for  post_id,media in data_list:

    a = [media_name for media_name, media_list in all_media_list if
         media in [i for i in media_list.split("|") if i != '']]
    if a:
        media_union = a[0].encode("gbk", 'ignore').decode("gbk", "ignore")
    else:
        media_union = media.encode("gbk", 'ignore').decode("gbk", "ignore")
    sql = f'update news2019_dyn set media_union = "{media_union}"  where post_id = {post_id} '
    cur.execute(sql)
    conn.commit()
    print(sql)