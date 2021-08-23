# import execjs
# with open("demo.js",'r',encoding="utf-8") as f:
#     js_file = f.read().strip()
#     print(js_file)
#
# text_ = 'ak+9VCsq4dEdB+UdVvGo8kh5JDEbMHGTCmF'
# js_code = execjs.compile(js_file,cwd=r'D:\代码脚本\项目程序\node_modules').call("_0x515f1e",text_)
#
# print(js_code)
import json
import os

import requests

url = "https://api.zzzmh.cn/bz/v3/getData"

# payload = "{\"size\":23,\"current\":0,\"sort\":0,\"category\":1,\"resolution\":0,\"color\":0,\"categoryId\":50}"
headers = {

  'Content-Length': '85',
  'Content-Type': 'application/json;charset=UTF-8',
  'Host': 'api.zzzmh.cn',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'sec-ch-ua-mobile': '?0',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
}

payload ={"size":23,"current":1,"sort":0,"category":0,"resolution":0,"color":0,"categoryId":50}



response = requests.request("POST", url, headers=headers, data=json.dumps(payload)).json()
result = response.get("result")
print(result)
# result =  "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"

js_file = os.popen('node demo.js {result}'.format(result='"'+result+'"'))
js_text = js_file.read().strip()
data_list = json.loads(js_text).get('list')
for item in data_list:
    pic_id = item["i"]
    pic_url = f'https://doge.zzzmh.cn/wallpaper/origin/{pic_id}.jpg/fhd'
    print(pic_url)

