from scrapy.cmdline import execute
import datetime

from scrapy.cmdline import execute
import datetime
d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '00:00', '%Y-%m-%d%H:%M')
d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '07:00', '%Y-%m-%d%H:%M')

# 当前时间
n_time = datetime.datetime.now()
print(n_time,d_time1,d_time)
if d_time1<n_time:

    execute('scrapy crawl update_tt'.split())
