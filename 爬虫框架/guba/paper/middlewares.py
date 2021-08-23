# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from collections import defaultdict

import requests
from scrapy import signals
from twisted.web._newclient import ResponseFailed
import json
import time
from .log_config import logger

from .Try_to_getProxy import ProxyModel

from twisted.internet.defer import DeferredLock


class Randomproxys(object):
    def __init__(self,proxy_url):
        self.proxy_url = proxy_url
        self.current_proxy = None  # 和最后的current_proxy对应
        self.lock = DeferredLock()
        self.start = True
        self.start_num = 0
        self.global_proxy = False

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings

        return cls(proxy_url=settings.get('PROXY_URL'),
        )

    def process_request(self, request, spider):
        if self.current_proxy ==None:
            return None
        else:
            if 'proxy' not in request.meta:
                self.update_proxy()  # 调用update更新代理，调用的时候对下面的update函数进行判断，如果三
                # 个条件都无法满足则一直使用一样的ip地址..
            #     # self.current_proxy.start_num +=1
            #     print('开始请求数据.....')
                request.meta['proxy'] = self.current_proxy




    def process_response(self,request,response,spider):
            print(self.current_proxy,'ip_代理.......',response.status,)

            if any (i in response.body.decode('utf8') for i in ['财经评论','投资必读'] ) \
                    or response.status in (403,503,504,407):
                print('新的代理产生....')
                self.current_proxy = None

                self.update_proxy()
                logger.info('%s新代理' % self.current_proxy)
                request.meta['proxy'] = self.current_proxy
                return request

            return response

    def process_exception(self, request, exception, spider):
            logger.info('Got exception:11111111111 %s' % (exception))

            # self.current_proxy.is_expiring = False
            self.current_proxy = None
            self.update_proxy()
            # logger.info('%s新代理' % self.current_proxy.proxy)
            request.meta['proxy'] = self.current_proxy
            return request

    def update_proxy(self):
        self.lock.acquire()
        #定义了初始变量current_proxy

        if not self.current_proxy:  # 更换ip这里的条件
            time.sleep(0.5)

            response = requests.get(self.proxy_url).json()
            # text = json.loads(response.text)
            if response:
                proxy = response.get("proxy")
                self.current_proxy = 'http://'+proxy
                # proxy = response.get("data")[0].get("IP") + ':' + str(response.get("data")[0].get("Port"))
                # self.current_proxy = 'http://' + proxy
                logger.info('重新获取了一个代理：%s' % self.current_proxy)
                # self.current_proxy = proxy_model#current_proxy这个时候就不会是NONE
        self.lock.release()
