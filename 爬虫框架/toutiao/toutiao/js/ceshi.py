import hashlib, os, time, requests, random


def get_signature(url, cookies):
    sign = os.popen('node _get_as_cp_signature.js {url} {cookies}'.format(url='"' + url + '"', cookies='"' + cookies + '"')).read()
    return sign


def parse(max_behot_time=0):
    headers = {
        'authority': 'www.toutiao.com',
        'sec-ch-ua': 'Google',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.toutiao.com/',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'ttcid=5383c7cd65124c279ea8627231ba07ce20; tt_webid=6932748630370256391; csrftoken=03eed9c57e1c13ede8ff0655484a0648; csrftoken=03eed9c57e1c13ede8ff0655484a0648; passport_csrf_token=4729b295111b1fc9c128e4f47179c0a5; __utmz=24953151.1615880696.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); FRM=new; PIXIEL_RATIO=1.5; __utma=24953151.1786946199.1615880696.1615880696.1617849239.2; WIN_WH=391_578; ttwid=1%7CKsJtLsS-oK5WbTn-fv37N6TkXnFSTSPYxsiGdINBDio%7C1618188472%7C5386f584537fd9ff3ee5558cd9371fd4926453b8e4ac8ed7e6699fa02c161c79; tt_webid=6940875644386870798; s_v_web_id=verify_kni5w5fl_39fbF25C_pYvx_4BP5_BS7G_obHIcPUDl9Bd; __ac_signature=_02B4Z6wo00f01-RTUpwAAIDAVKK-VwXhsZPkd1YAAJls5aDEmC4aBfzC7cqi.iH8VGS1h-HLz4p9OgmXdcOIr8HtWA63bTc69tqGYiJdh9MEOXIb-HA4un2TH7W5u3cqDdwwM9d03ZY9tMxO80; MONITOR_WEB_ID=81783b50-3db1-4cf4-9a7a-39242aa524ed; tt_scid=M3kynamAe9Wov9JjoA1V99HSpM.OEAvVP9FbzgTLBaPNgx-KCXh09wcIehyJV5ST6c86',
    }

    base_url = 'https://www.toutiao.com'

    if max_behot_time == 0:
        param = '/api/pc/feed/?min_behot_time=0&category=news_hot&utm_source=toutiao&widen=1&tadrequire=true'
    else:
        param = '/api/pc/feed/?max_behot_time={}&category=news_hot&utm_source=toutiao&widen=1&tadrequire=true'.format(
            max_behot_time)

    sign_url = "https://www.toutiao.com/toutiao/api/pc/feed/?category=profile_all&utm_source=toutiao&visit_user_token=MS4wLjABAAAArQbTPDWAI0qztKe118yJSQGmmX-NCHPdwF8dnTmZYVc&max_behot_time=0"
    signature = get_signature(sign_url, headers["cookie"]).replace('\n', '')
    print(signature)
    path = 'https://www.toutiao.com/api/pc/feed/?category=profile_all&utm_source=toutiao&visit_user_token=MS4wLjABAAAArQbTPDWAI0qztKe118yJSQGmmX-NCHPdwF8dnTmZYVc&max_behot_time=0&_signature=' + signature
    headers['path'] = path

    req_url = path
    print(req_url)
    # print(req_url)
    header = {
        'cookie': 'ttcid=5383c7cd65124c279ea8627231ba07ce20; tt_webid=6932748630370256391; csrftoken=03eed9c57e1c13ede8ff0655484a0648; csrftoken=03eed9c57e1c13ede8ff0655484a0648; passport_csrf_token=4729b295111b1fc9c128e4f47179c0a5; __utmz=24953151.1615880696.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); FRM=new; PIXIEL_RATIO=1.5; __utma=24953151.1786946199.1615880696.1615880696.1617849239.2; WIN_WH=391_578; ttwid=1%7CKsJtLsS-oK5WbTn-fv37N6TkXnFSTSPYxsiGdINBDio%7C1618188472%7C5386f584537fd9ff3ee5558cd9371fd4926453b8e4ac8ed7e6699fa02c161c79; tt_webid=6940875644386870798; s_v_web_id=verify_kni5w5fl_39fbF25C_pYvx_4BP5_BS7G_obHIcPUDl9Bd; __ac_nonce=06077d60a00fd64fa9987; __ac_signature=_02B4Z6wo00f01-RTUpwAAIDAVKK-VwXhsZPkd1YAAJls5aDEmC4aBfzC7cqi.iH8VGS1h-HLz4p9OgmXdcOIr8HtWA63bTc69tqGYiJdh9MEOXIb-HA4un2TH7W5u3cqDdwwM9d03ZY9tMxO80; MONITOR_WEB_ID=81783b50-3db1-4cf4-9a7a-39242aa524ed; tt_scid=M3kynamAe9Wov9JjoA1V99HSpM.OEAvVP9FbzgTLBaPNgx-KCXh09wcIehyJV5ST6c86; tt_webid=6939782229766915597',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'

    }

    response = requests.get(url=req_url,headers = header,
)
    print(response.json())
    # print(response.text)
'https://www.toutiao.com/api/pc/feed/?category=profile_all&utm_source=toutiao&visit_user_token=MS4wLjABAAAAQsfNjXJqZJRE1wOtBLJblyr5Dc9FxET3tGUccI-jqUGDyYHxR3O4uy483iiS3BUD&max_behot_time=0&_signature=_02B4Z6wo00f01XYWOlAAAIDCxufWmxRB0ol2Mj7AAD324PLdVw73IMd0p6heGnd5ywHe.xmg5RMklr1GNYS4D.rumPGWho8gVHPMKGEIDuEOLM.nMYoLKTnWRHUl1lGY0ivqi4pxgMsO.ZE227'
#     for k in response.json().get('data'):
#         k_dic = {}
#         k_dic['source'] = k.get('source')  # 发布账号
#         k_dic['behot_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(k.get('behot_time'))))  # 发布时间
#         k_dic['title'] = k.get('title')  # 文章标题
#         k_dic['source_url'] = 'https://www.toutiao.com' + k.get('source_url')  # 文章链接
#         print(k_dic)
#     next = response.json().get('next').get('max_behot_time')
#     print("next:", next)
#     if next != 0:
#         time.sleep(random.randint(3, 6))
#         print('--------即将抓取下一页--------')
#         parse(next)
#
#
if __name__ == '__main__':
    parse()
