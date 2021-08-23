from scrapy.cmdline import execute
import time
from scrapy.cmdline import execute
import datetime
d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '00:00', '%Y-%m-%d%H:%M')
d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '07:00', '%Y-%m-%d%H:%M')

# 当前时间
n_time = datetime.datetime.now()

if d_time1<n_time:

    execute('scrapy crawl tt_id'.split())
