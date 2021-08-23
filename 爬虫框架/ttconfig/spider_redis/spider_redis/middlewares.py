# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import gzip
import json
import random

from scrapy import signals
from twisted.internet.defer import DeferredLock
from twisted.internet.error import TimeoutError
class SpiderRedisSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UserAgentDownloadMiddleware():

    def __init__(self):
        # ua = UserAgent(use_cache_server=False)
        # print(ua,1111111)
        self.user_agents = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
                            ]
        # self.user_agents = self.ua
    def process_request(self,request,spider):#取名的process_request(request,spider),procecss_response(request,response,spider),process_exception
        a = self.user_agents
        self.header = random.choice(a)
        request.headers['User-Agent'] = self.header#中间件的时候一定要记得设置setting


class SpiderRedisDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        print('新的请求......')
        return None

    def process_response(self, request, response, spider):

        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
            print('Got exception:11111111111 %s' % (exception))
            # Called when a download handler or a process_request()
            # (from other downloader middleware) raises an exception.

            # Must either:
            # - return None: continue processing this exception
            # - return a Response object: stops process_exception() chain
            # - return a Request object: stops process_exception() chain
            # if isinstance(exception, TimeoutError):
            #     print(1111111111111111111111111111111)

            return request


    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
