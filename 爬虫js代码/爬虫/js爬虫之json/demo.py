import json

import demjson
import execjs
import requests


def get_jscode(filename):
    with open(filename, 'r',encoding='utf8') as f:
        jscode = f.read()
    return jscode




header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

url = 'https://unicom_trip.133.cn/api/v1/city/flight-route/SHA?date=20210608&type=dep'

response = requests.get(url,headers=header).text
jscode = get_jscode('demo_js.js')
result = execjs.compile(jscode).call('dataDecode',response)
data_list = result.get('data')
for item in data_list:
    dep_city_code = item.get('dep_city_code')
    arr_city_code = item.get('arr_city_code')
    print(dep_city_code,arr_city_code)

import time

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://unicom_trip.133.cn/city/?system=cjfcts")
browser.refresh()
time.sleep(1.5)
accessToken = browser.execute_script("return localStorage.getItem('flightList')")
browser.close()
print(accessToken)
