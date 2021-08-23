import pymysql
import scrapy
from furl import furl
from redis import Redis
from scrapy.utils.project import get_project_settings
from scrapy_splash import SplashRequest,SlotPolicy
import os
lua_script = '''
   function main(splash, args)

       splash:set_custom_headers({
           ["Cookie"] = "ttcid=c4a7a5b39b704b8ab8be262d7926786a30; csrftoken=74d859b1282c9f038209fbf30fe6cfa6; WEATHER_CITY=%E5%8C%97%E4%BA%AC; PIXIEL_RATIO=1.5; sso_uid_tt=3aab2c0d7e6b017b0ea25f2dc09e7ec4; sso_uid_tt_ss=3aab2c0d7e6b017b0ea25f2dc09e7ec4; toutiao_sso_user=6b202cdd3c7266fdee4250dd777c6c58; toutiao_sso_user_ss=6b202cdd3c7266fdee4250dd777c6c58; sid_guard=6d59bafe68b1d4985bbafd8acc5f815a%7C1594191164%7C5184000%7CSun%2C+06-Sep-2020+06%3A52%3A44+GMT; uid_tt=36eb4fca4ae8694c71028232f426bf92; sid_tt=6d59bafe68b1d4985bbafd8acc5f815a; sessionid=6d59bafe68b1d4985bbafd8acc5f815a; SLARDAR_WEB_ID=ec4a8dcb-db09-4fd9-922b-38879eb9a78b; UM_distinctid=1735a6621107d5-00bb1f0a596c86-b7a1334-e1000-1735a662112a2c; cp=5F3E0103051FAE1; uid_tt_ss=3aab2c0d7e6b017b0ea25f2dc09e7ec4; sessionid_ss=6b202cdd3c7266fdee4250dd777c6c58; WIN_WH=1280_578; __utmz=24953151.1599121320.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=24953151.1663346515.1599121320.1599123214.1599142088.3; tt_webid=6868447173950080520; tt_webid=6868447173950080520; s_v_web_id=verify_kep38i9e_bFX04JcO_CHgG_4VJv_8H8U_J09UIed1bie3; __ac_signature=_02B4Z6wo00f01j1rM9QAAIBCha1NiN.Qja49bjdAANAWRcznHlrCYM49sBHQRB.WZMAl9OUwgt-5Nv9h7N4jPr15uFsXv280u.zk3IWZGNEMaCuQglrgDx3Ip06SPEcgTc1CYZHg0A.YZjgkf0; MONITOR_WEB_ID=a2f4519d-d1db-4730-8f00-f352159a2c0b; tt_scid=2YO0rJaZ3.w2qKRXlauFH01Ub.Ih8Q.WJwGrduldyT.RqdPPnRcj7neInynXwAHCdf40"
       })
       splash.images_enabled = false
       assert(splash:go(args.url))
       assert(splash:wait(1))
       return {html = splash:html(),}
   end
   '''
class SPLAH(scrapy.Spider):
    name = 'splash_tt'

    allowed_domains = ['toutiao.com']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'toutiao.middlewares.UserAgentDownloadMiddleware': 500,
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.retry.RetryMiddleware':501,
            #ToutiaoSpiderMiddleware
            'toutiao.middlewares.ToutiaoDownloaderMiddleware':502,
            # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            # 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,

        },
        'SPIDER_MIDDLEWARES ':{
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
        }
    }

    start_urls = ['https://www.toutiao.com/c/user/token/MS4wLjABAAAAIVWtIwnW2GX65jXwycCOlsHINLkYO8mKUgXRfDlPPt0/']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.redis = Redis(host="tz6.zhangyupai.net", password="zz121212", port=6379, db=0)
        get_setting = get_project_settings()
        self.host = get_setting.get("MYSQL_HOST3")
        self.user = get_setting.get("MYSQL_USER3")
        self.password = get_setting.get("MYSQL_PASSWORD3")
        self.database = get_setting.get("MYSQL_DATABASE4")

    def start_requests(self):
        with open('id_.txt','r',encoding='utf8') as f:
            content_id = f.read().strip().split(",")
            self.id_ = min(content_id)
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8')
        self.cursor = self.db.cursor()  # 创建游标
        sql = '''select id, media,link from media where post_type = 0 and link !="" and id >=%s '''
        self.cursor.execute(sql,(self.id_))
        all_data_list = self.cursor.fetchall()
        for id_, meida, media_id in all_data_list:
            url = f'http://www.toutiao.com/c/user/{media_id}/'
            print(url,'网页的url的初始位置....')
            reslut = SplashRequest(url,
                endpoint='execute',
                args={'lua_source': lua_script,
                      },
                # cache_args=['lua_source'],

                callback=self.parse,   dont_filter=True,meta={'media':meida,'id_':id_})

            yield reslut

    def parse(self, response):

        All_datalist = response.xpath('''//div[@class='feed-list']/div''')

        for item in All_datalist:
            video  = item.xpath(".//div[@class='article-footer']//a/text()").get()

            toutiaourl = item.xpath(".//div[@class = 'title-box']/a/@href|.//div[@class='ugc-content']/a/@href").get()

            if toutiaourl == None:
                continue
            if 'a' in toutiaourl:
                f = furl(toutiaourl)
                path = r'/w/' + toutiaourl.split("/")[-1]

                f.path = path
                toutiaourl = f.url
            else:
                i_id = toutiaourl.split("/")[-2]
                if '播放' in video:
                    toutiaourl = 'https://www.ixigua.com/' + f'{i_id}'
                else:
                    toutiaourl = 'https://www.toutiao.com/' + f'i{i_id}/'


            self.redis.lpush('TTurl:start_urls', toutiaourl)
            print(toutiaourl)

