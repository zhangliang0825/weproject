import hashlib, os, time, requests, random


def get_signature(url, cookies):
    sign = os.popen('node _get_as_cp_signature.js {url} {cookies}'.format(url='"' + url + '"', cookies='"' + cookies + '"')).read()
    return sign


def parse(max_behot_time=0):
    headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'accept-encoding':'gzip, deflate, sdch, br',
'accept-language':'zh-CN,zh;q=0.8',
'cache-control':'max-age=0',
'cookie':'csrftoken=f0b1ad679f229da355e6c9ac522bb981; ttcid=d3084767ea704fefa6ddac7936408d3333; ttwid=1%7CEQqaQRGYqJHbM6vjddSmseATuLjWIh4Z9_nFPJ-svOk%7C1618548534%7C856d84a0502778e67a6e728a9e1cb2eba340d91e1bc2d4e72acdfcf1f4d6fbf1; s_v_web_id=verify_knju0apy_WuZ4QnO4_r0qq_47NW_ABUE_L5kmP4NhSpoX; __tasessionId=kvd80fygp1618558120604; csrftoken=f0b1ad679f229da355e6c9ac522bb981; csrftoken=f0b1ad679f229da355e6c9ac522bb981; MONITOR_WEB_ID=5b98e0f8-d2ce-4a39-ae1d-cc108629b7d7; tt_webid=6951613006950188581',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
       
    }

    base_url = 'https://www.toutiao.com'

    if max_behot_time == 0:
        param = '/api/pc/feed/?min_behot_time=0&category=news_hot&utm_source=toutiao&widen=1&tadrequire=true'
    else:
        param = '/api/pc/feed/?max_behot_time={}&category=news_hot&utm_source=toutiao&widen=1&tadrequire=true'.format(
            max_behot_time)
    for i in range(1,100):
        sign_url = "https://www.toutiao.com/toutiao/api/pc/feed/?category=profile_all&utm_source=toutiao&visit_user_token=MS4wLjABAAAAEcl6y-YFz8a8ncFOZrGU23SM4uGJi4fC9s_PLIQiptQ&max_behot_time=0"
        signature = get_signature(sign_url, headers["cookie"]).replace('\n', '')
        print(signature)
        path = 'https://www.toutiao.com/api/pc/feed/?category=profile_all&utm_source=toutiao&visit_user_token=MS4wLjABAAAAEcl6y-YFz8a8ncFOZrGU23SM4uGJi4fC9s_PLIQiptQ&max_behot_time=0&_signature=' + signature
        headers['path'] = path

        req_url = path
        print(req_url)
        # print(req_url)
        header = {
            'cookie': 'csrftoken=f0b1ad679f229da355e6c9ac522bb981; ttcid=d3084767ea704fefa6ddac7936408d3333; ttwid=1%7CEQqaQRGYqJHbM6vjddSmseATuLjWIh4Z9_nFPJ-svOk%7C1618548534%7C856d84a0502778e67a6e728a9e1cb2eba340d91e1bc2d4e72acdfcf1f4d6fbf1; s_v_web_id=verify_knju0apy_WuZ4QnO4_r0qq_47NW_ABUE_L5kmP4NhSpoX; __tasessionId=kvd80fygp1618558120604; csrftoken=f0b1ad679f229da355e6c9ac522bb981; csrftoken=f0b1ad679f229da355e6c9ac522bb981; MONITOR_WEB_ID=5b98e0f8-d2ce-4a39-ae1d-cc108629b7d7; tt_webid=6951613006950188581',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'

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
