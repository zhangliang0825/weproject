# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import csv
import os
import json
import logging
import random
import time
import scrapy
# from fake_useragent import UserAgent
from twisted.internet.defer import DeferredLock
from urllib import parse
from .Try_to_getProxy import ProxyModel
import requests
from scrapy.utils.python import global_object_name
from scrapy import signals
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from io import BytesIO
import gzip
from pyquery import PyQuery as pq

logger = logging.getLogger(__name__)
PROXY_URL = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=7&fa=1&groupid=0&fetch_key=&time=1&qty=1&port=1&format=json&ss=5&css=&dt=&pro=&city=&usertype=4&et=1'
class UserAgentDownloadMiddleware():

    def __init__(self):
        # ua = UserAgent(use_cache_server=False)
        # print(ua,1111111)
        self.user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
                            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
                            ]
        # self.user_agents = self.ua
    def process_request(self,request,spider):#取名的process_request(request,spider),procecss_response(request,response,spider),process_exception
        a = self.user_agents
        self.header = random.choice(a)
        request.headers['User-Agent'] = self.header#中间件的时候一定要记得设置setting


class MyretryMiddleware(RetryMiddleware):

    def process_response(self, request, response, spider):

        if request.meta.get('dont_retry', False):

            return response
        print(response,1231234123412222222222222222)
        print( request, response, spider)
        # result = json.loads(response)
        # print(result)
        # message = result.get("message")
        # print(message)
        # if message:
        #     reason = response_status_message(response.status)
        # #
        #     if  'sorry' in message:
        #         print(request.meta)
        #         return self._retry1(request, reason, spider) or response

        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception) \
                and not request.meta.get('dont_retry', False):
            # 删除该代理

            self.logger.warning('连接异常, 进行重试...')

            return self._retry1(request, exception, spider)

    def _retry1(self, request, reason, spider):
        retries = request.meta.get('retry_times', 0) + 1

        retry_times = self.max_retry_times

        if 'max_retry_times' in request.meta:
            retry_times = request.meta['max_retry_times']


        stats = spider.crawler.stats

        if retries <= retry_times:
            logger.debug("Retrying %(request)s (failed %(retries)d times): %(reason)s",
                         {'request': request, 'retries': retries, 'reason': reason},
                         extra={'spider': spider})

            # responses = requests.get(PROXY_URL)
            # data = json.loads(responses.text)
            # time.sleep(1)
            #
            # if len(data['data']) > 0:
            #     ip = data['data'][0]['IP']
            #     port = data['data'][0]['Port']
            #     proxy = 'https://' + '%s:%s' % (ip, port)
            #     print(proxy)
            #     request.meta['proxy'] = proxy
            #     print(request)
            retryreq = request.copy()
            retryreq.meta['retry_times'] = retries
            retryreq.dont_filter = True
            retryreq.priority = request.priority + self.priority_adjust


            if isinstance(reason, Exception):
                reason = global_object_name(reason.__class__)

            stats.inc_value('retry/count')
            stats.inc_value('retry/reason_count/%s' % reason)
            return retryreq
        else:
            stats.inc_value('retry/max_reached')
            logger.error("Gave up retrying %(request)s (failed %(retries)d times): %(reason)s",
                         {'request': request, 'retries': retries, 'reason': reason},
                         extra={'spider': spider})

class RandomProxy(object):
    def __init__(self,proxy_url):
        self.proxy_url = proxy_url
        self.current_proxy = None#和最后的current_proxy对应
        self.lock = DeferredLock()
        self.start = True
        self.start_num=0
        self.global_proxy = False

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings

        return cls(proxy_url=settings.get('PROXY_URL'),
                   )



    def process_request(self,request,spider):

            # if spider.name == 'sougou':
            #     return None
            # else:
                if 'proxy' not in request.meta or self.current_proxy.is_expiring:

                    self.update_proxy()#调用update更新代理，调用的时候对下面的update函数进行判断，如果三
                    # 个条件都无法满足则一直使用一样的ip地址..
                    # self.current_proxy.start_num +=1
                    request.meta['proxy'] = self.current_proxy.proxy
                    # request.meta['request_num'] = self.current_proxy.start_num

        #             print(request.meta,'meta参数.....')
        #             return None


    def process_response(self,request,response,spider):

        if spider.name =='webtt':
            buff = BytesIO(response.body)
            f = gzip.GzipFile(fileobj=buff)
            res = f.read().decode('utf-8')
            data_json = json.loads(res).get("dom")
            
            if data_json:

                doc = pq(data_json)("div.result-content").attr('cr-params')

                if not doc:
                    print(111111111111111111111112222,doc)
                    self.current_proxy.blacked = True
                    # if 'proxy' not in request.meta or self.current_proxy.is_expiring:
                    self.update_proxy()
                    request.meta['proxy'] = self.current_proxy.proxy
                    print(request.meta, 'response的请求信息')
                    return request
            return response
        if spider.name in ["tt_id_",'tt_id_','tt_id_2']:


            gzipfile = gzip.GzipFile('', 'rb', 9, BytesIO(response.body))
            res = gzipfile.read().decode('utf-8')
            # res = response.body.decode(response.encoding)
            # print(res,22222222221)
            if res!='':
                print(11111111111111111111111111133333)
                return  response
            else:
                print(22222222222222222222222233333333)
                self.current_proxy.blacked = True

                self.update_proxy()
                request.meta['proxy'] = self.current_proxy.proxy
                return request
        if  spider.name =='sougou':

            # buff = BytesIO(response.body)
            # f = gzip.GzipFile(fileobj=buff)
            # res = f.read()
            res = response.body.decode()
            if 'The URL has moved' in res:

                self.current_proxy.blacked = True

                self.update_proxy()
                request.meta['proxy'] = self.current_proxy.proxy
                return request
           
            # print(res, 11111111111111111111111666)
            return response


        else:
                buff = BytesIO(response.body)
                f = gzip.GzipFile(fileobj=buff)
                res = f.read().decode('utf-8')
                doc = pq(res)
                self.is_data_ip = doc('div.cs-view.cs-view-block').eq(0).remove('section')

                self.is_invaild_ = doc("div.tt-word1").text()
                if '抱歉，未找到' not in self.is_invaild_:
                    if not self.is_data_ip:

                        self.current_proxy.blacked = True
                    # if 'proxy' not in request.meta or self.current_proxy.is_expiring:
                        self.update_proxy()
                        request.meta['proxy'] = self.current_proxy.proxy

                        return request
                    # request.meta['request_num'] = self.current_proxy.start_num

                        # if ('proxy' in request.meta and not self.is_data_ip) or  self.current_proxy.is_expiring:
                        #     self.current_proxy.blacked = True
                        #     self.update_proxy()
                        #     request.meta['proxy'] = self.current_proxy.proxy
                        #     print(request.meta, '11111111response的第二次请求信息')
                        #     # request.meta['request_num'] = self.current_proxy.start_num
                        #     return request
                return response

    def process_exception(self, request, exception, spider):
            logger.info('Got exception:11111111111 %s' % (exception))
            # logger.info(f'成功....{self.current_proxy.is_expiring}')
            # self.current_proxy.is_expiring = False
            if not self.current_proxy.blacked:
                self.current_proxy.blacked = True
                self.update_proxy()

                logger.info('%s新代理' % self.current_proxy.proxy)
                request.meta['proxy'] = self.current_proxy.proxy
                return request


    def update_proxy(self):
        self.lock.acquire()
        #定义了初始变量current_proxy

        if not self.current_proxy or self.current_proxy.is_expiring\
                or self.current_proxy.blacked :#更换ip这里的条件
            time.sleep(1)
            # if self.global_proxy == False:
            #     proxy_url = self.proxy_url.get("proxy_url1")
            # else:
            proxy_url = self.proxy_url.get("proxy_url2")
            response = requests.get(proxy_url )
            text = json.loads(response.text)
            data_success = text.get("success")
            if data_success == 'false':
                self.global_proxy = True
                print(self.global_proxy,123123123)
            if len(text['data'])>0:
                data = text['data'][0]
                proxy_model = ProxyModel(data)
                logger.info('重新获取了一个代理：%s' % proxy_model.proxy)
                self.current_proxy = proxy_model#current_proxy这个时候就不会是NONE
        self.lock.release()



class locationproxy(object):
    def __init__(self, proxy_url):
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

        # if spider.name == 'sougou':
        #     return None
        # else:
        if 'proxy' not in request.meta:
            self.update_proxy()  # 调用update更新代理，调用的时候对下面的update函数进行判断，如果三
            # 个条件都无法满足则一直使用一样的ip地址..
            # self.current_proxy.start_num +=1
            request.meta['proxy'] = self.current_proxy
            print(request.meta,11111111111123312)
            # request.meta['request_num'] = self.current_proxy.start_num

    #             print(request.meta,'meta参数.....')
    #             return None

    def process_response(self, request, response, spider):
        if spider.name in ["tt_id", 'tt_id_', 'tt_id_2']:

            if  b'<html>' not in response.body:
                print(response.body[:50])
                gzipfile = gzip.GzipFile('', 'rb', 9, BytesIO(response.body))
                res = gzipfile.read().decode('utf-8')

                if res :

                    return response
                else:
                    self.current_proxy = None
                    print(22222222222222222222222233333333,res,3334444444456712)

                    # if 'proxy' not in request.meta or self.current_proxy.is_expiring:
                    self.update_proxy()
                    request.meta['proxy'] = self.current_proxy
                    return request
            else:
                print('出现了<html>............................')
                self.current_proxy = None
                # if 'proxy' not in request.meta or self.current_proxy.is_expiring:
                self.update_proxy()
                request.meta['proxy'] = self.current_proxy
                return request
        if spider.name == 'sougou':

            # buff = BytesIO(response.body)
            # f = gzip.GzipFile(fileobj=buff)
            # res = f.read()
            res = response.body.decode()
            print(res,11111111111111111111233123112)
            # print(res, 11111111111111111111111666)
            return response



    def process_exception(self, request, exception, spider):
        logger.info('Got exception:11111111111 %s' % (exception))
        self.current_proxy = None
        self.update_proxy()

        logger.info('%s新代理' % self.current_proxy)
        request.meta['proxy'] = self.current_proxy

    def update_proxy(self):
        self.lock.acquire()
        # 定义了初始变量current_proxy
        print('update proxy:',self.current_proxy)
        if not self.current_proxy:  # 更换ip这里的条件
            print('更换ip代理......')
            time.sleep(1)

            proxy_url = self.proxy_url.get("location")
            response = requests.get(proxy_url).json()
            proxy = 'http://'+response.get("proxy")
            self.current_proxy = proxy
            print(self.current_proxy,222222222222222222)
            # text = json.loads(response.text)
            # data_success = text.get("success")
            # if data_success == 'false':
            #     self.global_proxy = True
            #     print(self.global_proxy, 123123123)
            # if len(text['data']) > 0:
            #     data = text['data'][0]
            #     proxy_model = ProxyModel(data)
            #     logger.info('重新获取了一个代理：%s' % proxy_model.proxy)
            #     self.current_proxy = proxy_model  # current_proxy这个时候就不会是NONE
        self.lock.release()



class ToutiaoDownloaderMiddleware(RetryMiddleware):

    def __init__(self,proxy_url):
        self.proxy_url = proxy_url
        self.current_proxy = None#和最后的current_proxy对应
        self.lock = DeferredLock()
        # self.start = True
        self.start_num=0
        self.data_set = set()

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings

        return cls(proxy_url=settings.get('PROXY_URL'),
        )

    def process_request(self, request, spider):
        #
        print('经过起始的位置......')
        if 'proxy' not in request.meta['splash']['args'] or self.current_proxy.is_expiring:
            self.update_proxy()
            request.meta['splash']['args']['proxy'] = self.current_proxy.proxy

        # return None


    def process_response(self, request, response, spider):

        # doc = pq(response.body.decode("utf8"))
        #
        # all_text = doc("div.feed-list div.article-card")
        # print(all_text,12312312341234,response.status)
        print(response.status,1111111111111111111111222222222222222222222)
        if response.status in (503,504,400):
        #     if not all_text:
        #         print(all_text,1234567)
        # #         #当第一次请求过来的时候，如果无法请求response怎会进行ip的代理替换，每一次都会过来一个全新的resquest，如果都给封了进行替换
        # #         #替换的过程IP是不断的进行变化的，因为对ip替换的函数进行枷锁的限制，所有不会出现更多的ip减少开发的成本
        # #         #但这里还会出现一个问题就是如果代理的ip也被限制了，此时ip的锁还在怎会出现无法进行ip的替换
        #
        #         self.start_num +=1
        #         print(self.start_num)
        # #         print(self.start_num,1111111111111111222222223333333333333)
        # #         # spider.crawler.engine.close_spider(spider, "无有效信息，关闭spider")
        # #         # if 'proxy' not in request.meta['splash']['args'] or self.current_proxy.is_expiring:
                self.current_proxy.blacked = True
        # #         # if 'proxy' not in request.meta['splash']['args']:
                self.update_proxy()
                print(self.data_set,123123123123,request.meta['id_'])
                request.meta['splash']['args']['proxy'] = self.current_proxy.proxy
                print(request.meta)
        #         request.meta['readnum'] = self.start_num
        #         if self.start_num>10:
        #             spider.crawler.engine.close_spider(spider, "无有效信息，关闭spider")
        #             id_ = request.meta['id_']
        #             self.data_set.add(id_)
        #         with open('id_.txt','w',encoding='utf8',newline='') as f:
        #             writer = csv.writer(f)
        #             writer.writerow(self.data_set)
                return request
            # if  'proxy' in request.meta['splash']['args'] and  not all_text:
            #
            #     self.start_num += 1
            #     print(self.start_num, 111111111111111222222, '计数...........................')
            #     self.current_proxy.blacked = True
            #     self.update_proxy()
            #     request.meta['splash']['args']['proxy'] = self.current_proxy.proxy
            #     print(request.meta['splash']['args'], '第二次更换ip')
            #     return request
        return response

    def process_exception(self, request, exception, spider):
        logger.info('Got exception:11111111111 %s' % (exception))
        # logger.info(f'成功....{self.current_proxy.is_expiring}')
        # self.current_proxy.is_expiring = False
        if not self.current_proxy.blacked:
            self.current_proxy.blacked = True
            self.update_proxy()
            logger.info('%s新代理' % self.current_proxy.proxy)
            request.meta['proxy'] = self.current_proxy.proxy
            return request

    def update_proxy(self):
        self.lock.acquire()
        # 定义了初始变量current_proxy
        if not self.current_proxy or self.current_proxy.is_expiring \
                or self.current_proxy.blacked:  # 更换ip这里的条件
            time.sleep(1)
            # if self.global_proxy == False:
            #             #     proxy_url = self.proxy_url.get("proxy_url1")
            #             # else:
            #             #     proxy_url = self.proxy_url.get("proxy_url2")
            proxy_url = self.proxy_url.get("proxy_url2")
            response = requests.get(proxy_url)
            text = json.loads(response.text)
            data_success = text.get("success")
            if data_success == 'false':
                self.global_proxy = True
                print(self.global_proxy, 123123123)
            if len(text['data']) > 0:
                data = text['data'][0]
                proxy_model = ProxyModel(data)
                logger.info('重新获取了一个代理：%s' % proxy_model.proxy)
                self.current_proxy = proxy_model  # current_proxy这个时候就不会是NONE
        self.lock.release()