import datetime
import requests
# import traceback
import MySQLdb
from MySQLdb import cursors
from paper.log_config import logger

today = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
yesterday = datetime.datetime.strftime(datetime.datetime.now()+datetime.timedelta(-2), '%Y%m%d')

def old_urls_from_jijin_urls(link):
    link = link.replace('https://','http://')  # jijin_urls表内存储的url均为http开头
    for i in range(1,4):
        try:
            conn2 = MySQLdb.connect(host='120.26.106.222', user='julai01', password='Sh51785136@sh', database='jijin',
                                    charset='utf8mb4', cursorclass=cursors.SSCursor)
            with conn2.cursor() as cur:
                sql = "SELECT id FROM jijin_urls WHERE link=%s LIMIT 1 "
                cur.execute(sql, (link,))  # 注意格式
                data = cur.fetchone()
                if data == None:  # jijin_urls无数据返回，说明无oldurl
                    return False
                else:
                    return True
        except:
            logger.exception('select old urls error')
            continue

    logger.info('select old urls error more than three times')
    return False  # link查询出错超3次就选择入库


def old_urls():
    '''
    获取基金数据库昨天和今天的所有新闻url
    url没有http://和https://前缀
    '''
    old_urls_api = 'http://tz5.zhangyupai.net:8080/fund_old_urls'
    urls, md5s = set(), set()
    try:
        r = requests.get(old_urls_api, timeout=3)
        for url, md5link in r.json()['old_urls'].items():
            urls.add(url)
            md5s.add(md5link)
    except Exception as e:
        pass
    return urls, md5s


def old_urls_ano() ->set:
    '''
    获取数据库昨天和今天的所有的新闻url
    :return set()
    '''
    conn = MySQLdb.connect(host='120.26.106.222', user='julai01', password='Sh51785136@sh', database='jijin', charset='utf8mb4', cursorclass=cursors.SSCursor)
    try:
        with conn.cursor() as cur:
            sql = "select a.str_date, md5link from cx0308 a inner join hisinfo_cx b on a.id=b.post_id WHERE  b.id>8000000 and b.str_date>=%s"
            cur.execute(sql, (''.join(yesterday.split('-')),))  # 注意格式
            urls, md5s = set(), set()
            for url, md5 in cur:
                urls.add(url.replace('http://', '').replace('https://', ''))
                md5s.add(md5)
            return urls, md5s
    except:
        logger.exception('select old urls error')
        # traceback.print_exc()


# def old_urls():
#     '''
#     获取基金数据库昨天和今天的所有新闻url
#     url没有http://和https://前缀
#     '''
#     # old_urls_api = 'http://tz5.zhangyupai.net:8080/fund_old_urls'
#     # r = requests.get(old_urls_api)
#     r = {}
#     r["old_urls"] = {"xueqiu.com/9333035501/136611385": "2fe8490fd09ba8330772ef17a38ca440",
#                   "xueqiu.com/8876565794/136611444": "3e0036917f12ab4114a404e8a71ebc8f",
#                   "xueqiu.com/1184824257/136611564": "cb1be3692e9e3e45a011d7a3fc587b47",
#                   "xueqiu.com/7905095454/136611229": "ad7aa257f9da283cdcaa8427eaae536c",
#                   "xueqiu.com/S/SZ150290/136612021": "e4c4f84f62ee450d99793bc134e4b568",
#                   "xueqiu.com/S/OC836213/136612019": "a790ecff95fb52bc22e68fa7f39e445d",
#                   "xueqiu.com/S/SH603586/136612020": "1cbf79e7fc6ac789d574b9c734665bc6",
#                   "xueqiu.com/S/OC836213/136611500": "6e3f688e8b18bb7b0caf75a6d1f1e7b7",
#                   "xueqiu.com/S/EMQQ/136611502": "2dc7b03c3f5fc651aa9cf5799675faf5",
#                   "xueqiu.com/S/SH603586/136611501": "d6015af560cf8288c3c66ef49a378dd5",
#                   "xueqiu.com/1184824257/136611565": "099a5d2a8143bf667dc0864a1b86e76a",
#                   "xueqiu.com/5679199459/136612065": "c6beba55a69083f862d5e6e22778d917",
#                   "xueqiu.com/4730302029/136611994": "cbf297ab981414c9829c8fce0a2045e4",
#                   "xueqiu.com/1383591331/136611892": "d9d44c97006d45ecde32f2b600c4de01",
#                   "xueqiu.com/1283032256/136611718": "441ce2091165ed24978324307ebf52a2",
#                   "xueqiu.com/1021944347/136611675": "dda8ae3ea01186c13db4ebffd1aa386b",
#                   "xueqiu.com/6131303511/136611454": "301b38e840d6fe74a230231254d2a575",
#                   "xueqiu.com/1720238177/136611429": "471c1b2302acceed13c6338245782f0e",
#                   "xueqiu.com/2709154167/136611412": "cfe148bb5012263670f1fc41b281b94c",
#                   "xueqiu.com/S/OC836213/136612131": "048c26d9a3651ff56864da4c1036b140",
#                   "xueqiu.com/S/SH601066/136612133": "beb033197b6d982992a4a59d838fa4a6",
#                   "xueqiu.com/S/SH603586/136612132": "fe53e356a1f9b4adf4e7a44e71f754ef",
#                   "xueqiu.com/S/OC836213/136611671": "c64e36de7c9996bf35ac3ae4815f486b",
#                   "xueqiu.com/S/SH603586/136611672": "9855313d2c3c5f79678ca4e86bdae71c",
#                   "xueqiu.com/8894528164/136611231": "618847f702d4c0ddc71b8bb2a5056b55",
#                   "xueqiu.com/5952798513/136612166": "36fdfccde7e914347c9f5b7e63de2473",
#                   "toutiao.com/group/6765131710746067469/": "4c6c8ccde5021ef6b6d23df20dd5adec",
#                   "toutiao.com/group/6765131664625500679/": "c6602232662e99445a2f61ae656fc12d",
#                   "toutiao.com/group/6765131687270547982/": "c74cde299d79e9bf6c39ec59631a02e5",
#                   "xueqiu.com/9778139067/136611617": "9f02412e9675115b23d107ba239a65a1",
#                   "toutiao.com/group/6765130787093217805/": "0ec7fb0ec89d2a2a16f026bbd3b07354",
#                   "toutiao.com/group/6765130614644408840/": "db5da31f3f53c2cc67434d96c364212a",
#                   "weitoutiao.zjurl.cn/ugc/share/thread/1651646081729540/": "94e4260428361ffb22dc59da5d93e67a",
#                   "toutiao.com/group/6765149857532346894/": "b70787846e56d7bae2d96f80cfb1d7a5",
#                   "xueqiu.com/7183543114/136611756": "e7c2d7724f702d7a3f778068c36a4371",
#                   "toutiao.com/group/6765140101199561223/": "265a2b5a51cefba357d2092448fd58ae",
#                   "toutiao.com/group/6765144260648894983/": "39d66fc5f7659d645fc608ea032b9bf1",
#                   "toutiao.com/group/6765161604657971720/": "d929764405567623a8a3e57ddd5058c9",
#                   "toutiao.com/group/6765155947821138439/": "cf0ad3b1190500b2d7e9ecac63862e6a",
#                   "toutiao.com/group/6765155869739975176/": "26523111feef502b4dab3b64ad81f386",
#                   "toutiao.com/group/6765149674413228552/": "b6a40432dcd4da935ff0f5e10de08d88",
#                   "toutiao.com/group/6765146650110329357/": "e0e2076ac5fb650f84a158a722eef284",
#                   "toutiao.com/group/6765146512474243595/": "26555ad99021a011f9c8549a1ec6486c",
#                   "toutiao.com/group/6765144669442540040/": "d88743346a715d1d73a12ebe90b17b4b",
#                   "toutiao.com/group/6765139467943543310/": "b141115fcbf31c35acbf6a997c35060b",
#                   "toutiao.com/group/6765135293424075276/": "522a6b70f0b7833dcee00f7257e06677",
#                   "toutiao.com/group/6765131993203081742/": "34f8079ca1cca51eec3386be7d96843b",
#                   "toutiao.com/group/6765131704504943112/": "a3b4161f44390ca2a05453651181d1ae",
#                   "toutiao.com/group/6765130566854509069/": "d66f9ce7479de7c589c18f9e610b1ce1",
#                   "xueqiu.com/3100686462/136611297": "22b8e2ef1fa5ecc069e7b2a9ef466e66",
#                   "xueqiu.com/1151770036/136612182": "7482fdb43c9a2552aa7ce3db87a01105"}
#     urls, md5s = set(), set()
#     for url, md5link in r['old_urls'].items():
#         urls.add(url)
#         md5s.add(md5link)
#     return urls, md5s