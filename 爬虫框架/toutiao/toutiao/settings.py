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

BOT_NAME = 'toutiao'

SPIDER_MODULES = ['toutiao.spiders']
NEWSPIDER_MODULE = 'toutiao.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'toutiao (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1
RETRY_ENABLED = True
RETRY_TIMES = 5


# RETRY_HTTP_CODES = [404]  #重试
HTTPERROR_ALLOWED_CODES = [302]
# handle_httpstatus_list = [302]
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.9
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
    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
   # 'toutiao.middlewares.ToutiaoDownloaderMiddleware': 543,
    'toutiao.middlewares.UserAgentDownloadMiddleware':510,


}

REDIRECT_ENABLED = False
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
toutiaowebcookies = '_signature=_02B4Z6wo00f01OGiHuwAAICAYaDkrtyu-UzhhhpAAFl1ao758bva8sbo9uS67mHKHD3aOtzZOv1D-kiL1JfEVw3Z2kIaqbB8hgz8ANmAQa6FaQ4dbU.Jh46QdfTFgsnlqew3wRKCOC.kG8.Seb; __utmz=24953151.1615880696.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); FRM=new; PIXIEL_RATIO=1.5; ttcid=24f71fdb220943df99b38ee877c00c7511; sid_guard=da3c6a729bf88a41bd6a7855e710c63e%7C1618548299%7C5184000%7CTue%2C+15-Jun-2021+04%3A44%3A59+GMT; tt_webid=6940875644386870798; _S_DPR=1.5; _S_IPAD=0; __utma=24953151.1786946199.1615880696.1617849239.1622093895.3; _S_WIN_WH=1280_577; ttwid=1%7CKsJtLsS-oK5WbTn-fv37N6TkXnFSTSPYxsiGdINBDio%7C1627866018%7Ceaa32d32e251f8e238e1ff37cd661bf82af1a34e6196be045f815120ebd6cd4f; s_v_web_id=verify_c0def7b9b239ec7159fe6626be3d76cd; WIN_WH=252_577; MONITOR_WEB_ID=6940875644386870798; _signature=_02B4Z6wo00f01Eaog3AAAICAxqp5MYDS0qxGjIfAAHC0Ou1eBoqJV4KxEslvoezB.nXE61tFKmebI5vsDTg5LVklUZEcgT5D3KZ6O5TClLx1mUZH2G7zoJYhaXSs7CPs5ru7d9Mroa.t80v58f; tt_scid=Z8nTTCLB6Gx.f5dsNuongemvu31URY20-FA0BAcP2hmhSnTz.wz6QBKHicnPAmFo3739'
COOKIES_TT_WEB = BosstransCookie(toutiaowebcookies).stringToDict()

COOKIES_TT = 'ttcid=5383c7cd65124c279ea8627231ba07ce20; tt_webid=6932748630370256391; csrftoken=03eed9c57e1c13ede8ff0655484a0648; csrftoken=03eed9c57e1c13ede8ff0655484a0648; passport_csrf_token=4729b295111b1fc9c128e4f47179c0a5; __utmz=24953151.1615880696.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); FRM=new; PIXIEL_RATIO=1.5; __utma=24953151.1786946199.1615880696.1615880696.1617849239.2; WIN_WH=391_578; ttwid=1%7CKsJtLsS-oK5WbTn-fv37N6TkXnFSTSPYxsiGdINBDio%7C1618188472%7C5386f584537fd9ff3ee5558cd9371fd4926453b8e4ac8ed7e6699fa02c161c79; tt_webid=6940875644386870798; s_v_web_id=verify_kni5w5fl_39fbF25C_pYvx_4BP5_BS7G_obHIcPUDl9Bd; __ac_nonce=06077d60a00fd64fa9987; __ac_signature=_02B4Z6wo00f01-RTUpwAAIDAVKK-VwXhsZPkd1YAAJls5aDEmC4aBfzC7cqi.iH8VGS1h-HLz4p9OgmXdcOIr8HtWA63bTc69tqGYiJdh9MEOXIb-HA4un2TH7W5u3cqDdwwM9d03ZY9tMxO80; MONITOR_WEB_ID=81783b50-3db1-4cf4-9a7a-39242aa524ed; tt_scid=M3kynamAe9Wov9JjoA1V99HSpM.OEAvVP9FbzgTLBaPNgx-KCXh09wcIehyJV5ST6c86'
# COOKIES_TT = BosstransCookie(toutiaoiphonecookies).stringToDict()

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
ITEM_PIPELINES = {

    'scrapy_redis.pipelines.RedisPipeline': 300
}

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


# Enables scheduling storing requests queue in redis.
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

# Use this Scheduler, if your scrapy_redis version is <= 0.7.1
SCHEDULER = "scrapy_redis_bloomfilter.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis
DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"

# Redis URL


# Number of Hash Functions to use, defaults to 6
BLOOMFILTER_HASH_NUMBER = 6

# Redis Memory Bit of Bloom Filter Usage, 30 means 2^30 = 128MB, defaults to 30
BLOOMFILTER_BIT = 10
#
# # Persist
# SCHEDULER_PERSIST = True





REDIS_URL = 'redis://root:Lz@12@12@julai@tz6.zhangyupai.net:6379/10'

SPLASH_URL='http://127.0.0.1:8050/'
SPLASH_LOG_400 = True

DB_CONFIG = {
'host':'112.124.8.191',
        'port':3306,
        'user':'root',
        'password':'Zycj@2020688',
        'db':'toutiao',
        'charset':'utf8mb4'
}



