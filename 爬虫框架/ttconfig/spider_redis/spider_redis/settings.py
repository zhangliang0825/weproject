# -*- coding: utf-8 -*-

# Scrapy settings for spider_redis project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from datetime import datetime

from .get_cookies import TransCookie
BOT_NAME = 'spider_redis'

SPIDER_MODULES = ['spider_redis.spiders']
NEWSPIDER_MODULE = 'spider_redis.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'spider_redis (+http://www.yourdomain.com)'
RETRY_ENABLED = True


# Obey robots.txt rules
ROBOTSTXT_OBEY = False
RETRY_TIMES = 5
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 20
ALLOWED_CODES = [301]
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',


  'cache-control': 'max-age=0',

  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}


tt_cookies = 'ttcid=c4a7a5b39b704b8ab8be262d7926786a30; csrftoken=74d859b1282c9f038209fbf30fe6cfa6; WEATHER_CITY=%E5%8C%97%E4%BA%AC; PIXIEL_RATIO=1.5; sso_uid_tt=3aab2c0d7e6b017b0ea25f2dc09e7ec4; sso_uid_tt_ss=3aab2c0d7e6b017b0ea25f2dc09e7ec4; toutiao_sso_user=6b202cdd3c7266fdee4250dd777c6c58; toutiao_sso_user_ss=6b202cdd3c7266fdee4250dd777c6c58; sid_guard=6d59bafe68b1d4985bbafd8acc5f815a%7C1594191164%7C5184000%7CSun%2C+06-Sep-2020+06%3A52%3A44+GMT; uid_tt=36eb4fca4ae8694c71028232f426bf92; sid_tt=6d59bafe68b1d4985bbafd8acc5f815a; sessionid=6d59bafe68b1d4985bbafd8acc5f815a; SLARDAR_WEB_ID=ec4a8dcb-db09-4fd9-922b-38879eb9a78b; UM_distinctid=1735a6621107d5-00bb1f0a596c86-b7a1334-e1000-1735a662112a2c; cp=5F3E0103051FAE1; uid_tt_ss=3aab2c0d7e6b017b0ea25f2dc09e7ec4; sessionid_ss=6b202cdd3c7266fdee4250dd777c6c58; WIN_WH=1280_578; __utmz=24953151.1599121320.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=24953151.1663346515.1599121320.1599123214.1599142088.3; tt_webid=6868447173950080520; tt_webid=6868447173950080520; MONITOR_WEB_ID=de448bb0-ac46-4e8c-b84e-8fafeffd7689; __ac_signature=_02B4Z6wo00f01LYUYzQAAIBADtIdagdq3aS2EGeAAHLeOPOSnos3fnTx-hccJsUmEqg5LWKJoLiE6ODtAI28NOPU12T.02rCNM.PpSiR.dzThMBacQ6JWu5Im6RsshlpNLrTndicsmaCM14pa3; __tasessionId=591spwbw91599275316316; s_v_web_id=verify_kep38i9e_bFX04JcO_CHgG_4VJv_8H8U_J09UIed1bie3; tt_scid=v2qROtNFlklHiqvBcomq9EPUgzzTnt5M2p--4XuKx07Lrrm8.3VKYGE2zQk4bcFa670c; tt_webid=6835446038360000013; tt_webid=6835446038360000013; __ac_nonce=05f5301d3003f5b722c6a'

COOKIES_TT = TransCookie(tt_cookies).stringToDict()
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   # 'spider_redis.middlewares.UserAgentDownloadMiddleware': 200,
   # ' scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'spider_redis.middlewares.SpiderRedisDownloaderMiddleware': 543,
   #  'spider_redis.middlewares.Randomproxy': 542,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'spider_redis.pipelines.SpiderRedisPipeline': 300,
}

SCHEDULER_PERSIST = True

MYEXT_ENABLED=True      # 开启扩展
IDLE_NUMBER=360           # 配置允许的空闲时长，每5秒会增加一次IDLE_NUMBER，直到增加到360，程序才会close

# LOG_LEVEL = 'DEBUG'
# to_day = datetime.now()
# log_file_path = 'log/scrapy_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
# LOG_FILE = log_file_path


# # 在 EXTENSIONS 配置，激活扩展
# EXTENSIONS= {
#             'scrapy_redis.extensions.RedisSpiderSmartIdleClosedExensions': 500,
#         }

# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"



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

# REDIS_URL = 'redis://root:Lz@12@12@12@@tz6.zhangyupai.net:6379/8'
PROXY_URL = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&groupid=0&fetch_key=&time=100&qty=1&port=1&format=json&ss=5&css=&dt=0&pro=&city=&usertype=4&et=1'
MYSQL_HOST3 = '120.26.106.222'
MYSQL_USER3= 'julai01'
MYSQL_PASSWORD3 = 'Sh51785136@sh'
MYSQL_DATABASE4 = 'jijin'

MYSQL_HOST2 = '112.124.8.191'
MYSQL_USER2 = 'root'
MYSQL_PASSWORD2 = 'Zycj@2020688'
MYSQL_DATABASE3 = 'tuisong'
