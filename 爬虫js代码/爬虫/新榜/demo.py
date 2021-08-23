import random

import execjs
import requests


def FloatToHex(number, base = 16):
    if number < 0:                          # Check if the number is negative to manage the sign
        sign = "-"                          # Set the negative sign, it will be used later to generate the first element of the result list
        number = -number                    # Change the number sign to positive
    else:
        sign = ""                           # Set the positive sign, it will be used later to generate the first element of the result list

    s = [sign + str(int(number)) + '.']     # Generate the list, the first element will be the integer part of the input number
    number -= int(number)                   # Remove the integer part from the number

    for i in range(base):                   # Iterate N time where N is the required base
        y = int(number * 16)                # Multiply the number by 16 and take the integer part
        s.append(hex(y)[2:])                # Append to the list the hex value of y, the result is in format 0x00 so we take the value from postion 2 to the end
        number = number * 16 - y            # Calculate the next number required for the conversion

    return ''.join(s).rstrip('0')
result = FloatToHex(random.random())
print(result[-9:])

a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
for i in range(0,500):
    c = ''
    for j in range(0,9):
        e = int(random.random()*16)
        c += a[e]
url = f'/xdnphb/main/v1/week/rank?AppKey=joker&end=2021-06-10&rank_name=文化&rank_name_group=生活&start=2021-06-07&nonce={c}'
with open('js_xinbang.js', 'r') as f:
    js_text = f.read()

    js_code = execjs.compile(js_text).call('b',url)
    print(js_code)
data = {
'end':'2021-06-10',
'rank_name':'文化',
'rank_name_group':'生活',
'start':'2021-06-07',
'nonce':c,
'xyz':js_code,
}
print(data)
headers = {'accept':'application/json, text/javascript, */*; q=0.01',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
'cache-control':'no-cache',
'content-length':'148',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'cookie':'Hm_lvt_a19fd7224d30e3c8a6558dcb38c4beed=1623846536; UM_distinctid=17a14cbc89c268-0b6435e37b1495-3373266-e1000-17a14cbc89d160; token=3331815CA89E4EB6A3B852A5280E53C4; Hm_lpvt_a19fd7224d30e3c8a6558dcb38c4beed=1623856136; __root_domain_v=.newrank.cn; _qddaz=QD.149523856138898; CNZZDATA1253878005=1551295416-1623841574-https%253A%252F%252Fwww.baidu.com%252F%7C1623852394; _qdda=3-1.1; _qddab=3-rxha0i.kpzm0xb7',
'origin':'https://www.newrank.cn',
'pragma':'no-cache',
'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
'sec-ch-ua-mobile':'?0',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
'x-requested-with':'XMLHttpRequest',
    
}

post_url = 'https://www.newrank.cn/xdnphb/main/v1/week/rank'

response = requests.post(post_url,headers=headers,data=data)
print(response.text)