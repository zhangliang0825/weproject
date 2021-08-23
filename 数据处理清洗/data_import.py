import csv
import re
from itertools import islice
import pymysql
DB_CONFIG = {
'host':'112.124.8.191',
        'port':3306,
        'user':'root',
        'password':'Zycj@2020688',
        'db':'toutiao',
        'charset':'utf8mb4'
}


conn = pymysql.connect(**DB_CONFIG)
cursor = conn.cursor()
sql = '''insert into words (`key`, word,datetime) values (%s,%s,%s)'''

filename = csv.reader(open('key.csv', 'r',encoding="utf-8"))
dict_ = {}
for key,values,index_ in islice(filename , 1, None):
    dict_.setdefault(key,[]).append(values.split("\\\n"))
for key,vvalues in dict_.items():

    keyword_list = [i.split("\n")  for i in vvalues[0] if i !='']
    keyword_list = filter(lambda x:x!='',list(map(lambda x:x[0] ,keyword_list)))
    for info in keyword_list:
        try:
            keyword = re.sub(r'\[100\]|\(|\)|）|（','',info)
            print(key,info,keyword)
            cursor.execute(sql, (key, keyword,'20210810'))
            conn.commit()
            print(key,keyword)
        except Exception as e:
            print(e)


