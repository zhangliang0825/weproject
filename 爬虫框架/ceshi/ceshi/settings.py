# -*- coding: utf-8 -*-

# Scrapy settings for toutiao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from datetime import datetime

'''#! /usr/bin/bash
cd  /root/roots/fubencopy
/usr/bin/python import_zjx_12time_data.py
'''

from .Get_cookies import BosstransCookie

BOT_NAME = 'ceshi'

SPIDER_MODULES = ['ceshi.spiders']
NEWSPIDER_MODULE = 'ceshi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'toutiao (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS =8
RETRY_ENABLED = True
RETRY_TIMES = 8


# RETRY_HTTP_CODES = [404]  #重试
HTTPERROR_ALLOWED_CODES = [302,301,404]
handle_httpstatus_list = [302,301]
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   # 'toutiao.middlewares.ToutiaoSpiderMiddleware': 543,

}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
   # 'toutiao.middlewares.ToutiaoDownloaderMiddleware': 543,
   #  'ceshi.middlewares.UserAgentDownloadMiddleware':510,


}
from scrapy.downloadermiddlewares.retry import RetryMiddleware
REDIRECT_ENABLED = False
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

toutiaowebcookies = 'tt_webid=6999810541595182599; WIN_WH=1280_577; PIXIEL_RATIO=1.5; FRM=new; s_v_web_id=verify_6b5559a9c1af5a7c2813150f100c90e4; MONITOR_WEB_ID=6999810541595182599; _signature=_02B4Z6wo00f01LqQFkwAAICAOpLsDeTlACS6sBLAAE-Fa8; ttcid=9becd88c89c542c39e76842f2f0abe9276; tt_scid=a.7T0OfXUOWzXU6ybFxu-43KdUiQCJPmYmhTPRIuqV4xemDZEpPl2MU7VFlURuVzc9ce'
COOKIES_TT_WEB = BosstransCookie(toutiaowebcookies).stringToDict()

COOKIES_TT = 'csrftoken=f0b1ad679f229da355e6c9ac522bb981; ttcid=d3084767ea704fefa6ddac7936408d3333; s_v_web_id=verify_knqxlh0u_s3pQDeyd_5O6x_4feR_BWDr_tTRaqJrlsRIr; csrftoken=f0b1ad679f229da355e6c9ac522bb981; __ac_nonce=0608036b7006a98ba2dbc; __ac_signature=_02B4Z6wo00f01fYZ6MgAAIDCupW97Sk.Y9H2PexAAB0I5d; MONITOR_WEB_ID=3966c7e3-725e-4eb6-b131-274771bed1b6; ttwid=1%7CEQqaQRGYqJHbM6vjddSmseATuLjWIh4Z9_nFPJ-svOk%7C1619015616%7Ccb787cc3f66e8bbc01c2200c1543c398bc0faec533632bc382d105ef10b81266; csrftoken=f0b1ad679f229da355e6c9ac522bb981; tt_webid=6951613006950188581'
COOKIES_TT_JS = BosstransCookie(COOKIES_TT).stringToDict()

toutiaoweb2cookies = '_signature=_02B4Z6wo00f01rvrm5gAAICBCxp3UmIVh2K7z58AAM6XRxWo3OX5uqzb0NZehMm2D5dw77N4p.tcCS40Cb7xnLqYOO.dk4QzbntrwjkTGloAQDh6BHbEETDh64qHubm7CDEM.CkZP84JKzCEbd; tt_webid=6932748630370256391; passport_csrf_token=4729b295111b1fc9c128e4f47179c0a5; __utmz=24953151.1615880696.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PIXIEL_RATIO=1.5; FRM=new; ttcid=24f71fdb220943df99b38ee877c00c7511; MONITOR_WEB_ID=6932748630370256391; __utma=24953151.1786946199.1615880696.1615880696.1617849239.2; s_v_web_id=verify_kn9zvo3o_ftmS9PkE_plao_4iXA_85w4_LewLtc39aCcA; WIN_WH=391_578; _signature=_02B4Z6wo00f01jSEUmwAAICBhHW-pHVxHro0oFbAAO1fgM4ucDYWxwzsWJqYIXDMdFpDCx5sNAucsOE9H.iOtGOCU5K.aEM6WS91t1-CwRV4b6fbORKwtb9gNOwJ6m9J9.i2yVsbSL65esAwc4; tt_scid=o.wa4JoYV6a9AVXH7nu.UjRw8xfrtM4caQUI5iRSrnfqBrp7QWrPCUWBBVE1ScYj4a72'
COOKIES_TT_WEB2 = BosstransCookie(toutiaoweb2cookies).stringToDict()

toutiaoupdatehao = 'ttcid=5383c7cd65124c279ea8627231ba07ce20; tt_webid=6932748630370256391; csrftoken=03eed9c57e1c13ede8ff0655484a0648; tt_webid=6932748630370256391; csrftoken=03eed9c57e1c13ede8ff0655484a0648; passport_csrf_token=4729b295111b1fc9c128e4f47179c0a5; __utmz=24953151.1615880696.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); FRM=new; PIXIEL_RATIO=1.5; WIN_WH=244_578; __utma=24953151.1786946199.1615880696.1615880696.1617849239.2; __ac_signature=_02B4Z6wo00f01D9rBZQAAIDDj5rpXyoUDug.TwEAAG-8yxBXwKfjcmnX8Y1pEr8CA8EU14Z83xBn-hr8sj80RTScu3j1V2UJIi9O-uFFkX.Mi06BcY0kMJbTEXdr69p1hS1D3Dyj7qvukfT4a5; s_v_web_id=verify_kn9ni91i_I92KR6Hd_4dyA_48Mu_8tzm_5SzBIQ6iU8p8; __tasessionId=c1rq1hr5w1617936747655; MONITOR_WEB_ID=140cb8ff-b860-4f53-84a6-dbe275a13bf2; tt_scid=0.ycCl6VUGIJRsT.xNHEeDBfzFirFIJaYq5XOwQP89RvU9g3uHFpGEW-VA7JLuVg2c0c'
COOKIES_TT_UPDATE = BosstransCookie(toutiaoupdatehao).stringToDict()
# LOG_LEVEL = 'DEBUG'
# to_day = datetime.now()
# log_file_path = 'log/scrapy_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
# LOG_FILE = log_file_path
# # 日志编码
# LOG_ENCODING = 'utf-8'
# 如果是True ，进程当中，所有标准输出（包括错误）将会被重定向到log中;例如：在爬虫代码中的 print（）
# LOG_STDOUT = True  # 默认为False

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#
#     'scrapy_redis.pipelines.RedisPipeline': 300
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# # Enables scheduling storing requests queue in redis.
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # Ensure all spiders share same duplicates filter through redis.
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

PROXY_URL = {'proxy_url1':'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=7&fa=1&groupid=0&fetch_key=&time=1&qty=1&port=1&format=json&ss=5&css=&dt=&pro=&city=&usertype=4&et=1',
             'proxy_url2':'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&groupid=0&fetch_key=&time=100&qty=1&port=1&format=json&ss=5&css=&dt=0&pro=&city=&usertype=4&et=1',
             'location':'http://tz2.zhangyupai.net:5010/get/'}
#月

# PROXY_URL2 = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&groupid=0&fetch_key=&time=100&qty=1&port=1&format=json&ss=5&css=&dt=0&pro=&city=&usertype=4&et=1'
#次
REDIS_URL = 'redis://root:Lz@12@12@julai@tz6.zhangyupai.net:6379/8'

SPLASH_URL='http://127.0.0.1:8050/'
SPLASH_LOG_400 = True
MYSQL_HOST3 = '112.124.8.191'
MYSQL_USER3= 'root'
MYSQL_PASSWORD3 = 'Zycj@2020688'
MYSQL_DATABASE4 = 'toutiao'
MYSQL_DATABASE5 = 'tuisong'


MYSQL_HOST = '120.26.106.222'
MYSQL_USER = 'julai01'
MYSQL_PASSWORD = 'Sh51785136@sh'
MYSQL_DATABASE = 'jijin'
