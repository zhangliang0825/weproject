from selenium import webdriver
import time
from pprint import pprint
import redis

def log_weixin(useres,passwordes):
    pool = redis.ConnectionPool(host='tz6.zhangyupai.net', port=6379,db=1,password='Lz@12@12@julai')
    r = redis.Redis(connection_pool=pool)
# dict_ = {'876a7afb547e67a878d6277a4ae3d262':'[1112rrr3www11111,kkkkkkkkkkkkkkkkk]',}
# r.set('7e6306769c95bdc44e199ca2dd2b5faa',dict_)

    cookie = {}
    url = 'https://mp.weixin.qq.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    dianji = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[2]/a')
    dianji.click()
    time.sleep(0.5)
    user = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[1]/div/span/input')
    password = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[1]/div[2]/div/span/input')
    user.clear()
    user.send_keys(useres)
    password.clear()
    password.send_keys(passwordes)
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div[1]/form/div[4]/a').click()
    # driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[4]/a').click()
    time.sleep(12)



    cookies = driver.get_cookies()
    driver.close()
    for item in cookies:
        cookie[item.get('name')] = item.get('value')
        r.set(useres,cookie)
    print(cookie)

def mian():
    # name = ['748502278@qq.com', '2324575031@qq.com']
    name = ['1778720144@qq.com','1830182528@qq.com','1419774804@qq.com','2245382721@qq.com','2730590293@qq.com']
    # name = ['1830182528@qq.com']
    # sumbit = ['shinichi91041', 'shinichi91041']
    sumbit = ['zaqqaz123456','zz121212','zz121212','zz121212','zz121212']
    # sumbit = ['zz121212']
    for name,word in zip(name,sumbit):
        time.sleep(1)
        log_weixin(name,word)

if __name__ == '__main__':
    mian()







































