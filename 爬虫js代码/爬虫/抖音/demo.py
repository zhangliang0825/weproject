
import time

import requests
from datetime import datetime,timedelta

yesterday = datetime.today()+timedelta(-1)

yesterday_str = yesterday.strftime('%Y%m%d')
print(yesterday_str)
word_list = [
'新华基金','华安基金','景顺长城','中信保诚','博时基金','嘉实基金','南方基金','天弘基金','兴证全球基金','建信基金','汇添富基金','鹏华基金','民生加银基金','交银施罗德','银华基金','招商基金','天弘基金','华安基金','鹏华基金','中欧基金','东方红资产管理','国泰元鑫',
'富国基金','平安基金','中邮基金','东证资管','新华基金','华商基金','华夏基金', '易方达基金','工银瑞信基金','海富通基金','华宝基金'
#             '富国基金',
           ]
insert_url = 'http://tz4.zhangyupai.net:81/mobile/import_news1.php'
for name in word_list:
    web_url = f'https://www.douyin.com/aweme/v1/web/search/item/?device_platform=webapp&aid=6383&channel=channel_pc_web&search_channel=aweme_video_web&sort_type=0&publish_time=1&keyword={name}&search_source=search_history&query_correct_type=1&is_filter_search=1&offset=0&count=24&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F92.0.4515.107+Safari%2F537.36&browser_online=true'
    print(web_url)

    headers = {

    'cache-control':'no-cache',
    'cookie':'s_v_web_id=verify_c5985ddf1280fd05542685e504be21ab',
    'pragma':'no-cache',
    'referer':'https://www.douyin.com/search/%E5%AF%8C%E5%9B%BD%E5%9F%BA%E9%87%91?publish_time=1&sort_type=0&source=search_history&type=video',
    'sec-ch-ua':'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile':'?0',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'withcredentials':'true',

    }


    response = requests.get(web_url, headers=headers).json()
    data_list = response.get("data")
    for item in data_list:
        item_data = {}

        aweme_info = item.get("aweme_info")
        nickname = aweme_info.get("author").get("nickname")
        desc = aweme_info.get("desc")
        aweme_id = aweme_info.get("aweme_id")
        dy_url = f'https://www.douyin.com/video/{aweme_id}'
        title = desc
        create_time = aweme_info.get("create_time")
        titme_stap = time.localtime(create_time)
        publish_time = time.strftime('%Y%m%d',titme_stap)
        if yesterday_str <= publish_time:
            item_data['title'] = title
            item_data["summary" ] = desc
            item_data["media_orig" ] =nickname
            item_data['content'] = desc+name
            item_data['str_date'] = publish_time
            item_data['content_url'] = dy_url+'?dyhao'
            item_data["media" ] = '抖音'
            item_data["post_type" ] = 21
            for i in range(1, 10):
                print(i, '页数...')
                try:

                    res = requests.post(insert_url, data=item_data, timeout=12).text
                    print(res)
                    if '1' in str(res):
                        break

                except Exception as e:
                    print(e)
            print(222222222222222222011111111114444)

            print(title,nickname, desc,aweme_id,dy_url,publish_time)


# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
#
# driver.get('https://www.douyin.com/video/6986594699146513677?previous_page=search_result?http://v3-web.douyinvod.com/99ef8bc150e00e34909b59e19219474f/60f63725/video/tos/cn/tos-cn-ve-15/758508af345049c8a055ac9d3dbd8835/?a=6383&br=646&bt=646&cd=0%7C0%7C0&ch=11&cr=0&cs=0&dr=0&ds=3&er=&ft=fTbd.fHH_MZi85gkag31r5CYj9-w&l=202107200934240102121980513402BC8D&lr=all&mime_type=video_mp4&net=0&pl=0&qs=0&rc=anNmNWU6ZmlvNjMzNGkzM0ApMzM2OztkOGRmNzVnN2VnZWcuNl8tcjRfbW5gLS1kLTBzcy0vMTQvYV42Ml8wYWBfXy06Yw%3D%3D&vl=&vr=')
