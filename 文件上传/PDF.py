#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Download a webpage as a PDF."""
import time

from selenium import webdriver

def format_web(url,name):

    driver = webdriver.PhantomJS('phantomjs')
    if 'week' in url :
        driver.maximize_window()
    # elif 'quarterindex' in url:
    #     driver.set_window_size(800, 2800)
    else:
        driver.set_window_size(700, 600)#日报
    # driver.set_window_size(780,1)
    # driver.maximize_window()
    driver.get(url)
    time.sleep(6)
    download(driver, "{}.pdf".format(name))
    return '转化成功..'

def download(driver, target_path):
    """Download the currently displayed page to target_path."""
    
    def execute(script, args):
        driver.execute('executePhantomScript',
                       {'script': script, 'args': args})


    # hack while the python interface lags
    driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')

    if 'zhoubao' in target_path:
        page_format = 'this.paperSize = {format: "A4", orientation: "portrait"};'#,font-family: "serif"
    else:
        page_format = 'this.paperSize = {format: "A4", orientation: "portrait",font-family: "serif"};'
    execute(page_format, [])
    # render current page
    render = '''this.render("{}")'''.format(target_path)
    execute(render, [''])


# if __name__ == '__main__':
#     url = 'http://www.zhangyupai.net/mobile/weekindex_1030.php?key1=%E4%B8%9C%E8%AF%81%E8%B5%84%E7%AE%A1&print=1'
#     result =  format_web(url,'20210514zhoubaodzzg')
    

