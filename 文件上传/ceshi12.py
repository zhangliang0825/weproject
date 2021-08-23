import requests
import pymysql
from PDF import format_web

dbhost3 = '120.26.106.222'
dbuser3 = 'julai01'
passwd3 = 'Sh51785136@sh'
dbname3 = 'jijin'

conn3 = pymysql.connect(dbhost3, dbuser3, passwd3, dbname3, charset='utf8')
cur3 = conn3.cursor()
sql = 'select key1,str_date,reportcat from hisrisk_week'
cur3.execute(sql)
data_list = cur3.fetchall()

for key1,str_date,reportcat in data_list:
    if 'week' in reportcat and key1 =='富国' and '2020' in str_date:
        print(key1,str_date,reportcat)
        url = 'http://www.zhangyupai.net/mobile/weekindex_1030.php?key1=%E5%AF%8C%E5%9B%BD&print=1&preview=&clientview=&str_date={}'.format(str_date)
        'http://www.zhangyupai.net/mobile/weekindex_1030.php?key1=%E5%AF%8C%E5%9B%BD&print=&preview=&clientview=&str_date=20200421'
        print(url)
        save_name = str_date + 'zhoubao'
        result = format_web(url, save_name)
        Shh_jiji_name = str_date+'富国基金每周报告'

        files = {

            'file': open(r'{}.pdf'.format(save_name), 'rb'),

        }


        data = {
            "token": '{"path":"/var/www/html/jijin/upload/%s/","name":"%s"}' % ('fullgoal', Shh_jiji_name)
        }
        response = requests.post('http://www.zhangyupai.net:8181/uploadfile/',
                                 files=files, data=data).text
        print(response)
