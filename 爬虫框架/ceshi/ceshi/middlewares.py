

import time

import demjson
from twisted.internet.defer import DeferredLock

import requests

from scrapy import signals

from io import BytesIO
import gzip
from pyquery import PyQuery as pq
from scrapy.downloadermiddlewares.retry import RetryMiddleware,\
    get_retry_request


class GetFailedrequsts(RetryMiddleware):
    def __init__(self, settings):
        self.max_retry_times = settings.getint('RETRY_TIMES')
        self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
        self.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')

    def process_response(self, request, response, spider):

        responses = response.body.decode("utf8")
        response_json = demjson.decode(responses).get("data")

        if response_json == None:
            print('进行重试的新请求数据..')
            print(response_json)
            return self._retry(request, 'spider error', spider) or response

        return response

    def _retry(self, request, reason, spider):
        max_retry_times = request.meta.get('max_retry_times', self.max_retry_times)
        priority_adjust = request.meta.get('priority_adjust', self.priority_adjust)
        return get_retry_request(
            request,
            reason=reason,
            spider=spider,
            max_retry_times=max_retry_times,
            priority_adjust=priority_adjust,
        )


class CeshiSpiderMiddleware:
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

    def get_random_cookies(self):
        url = 'https://v.sogou.com/'

        rst = requests.get(url=url,

            allow_redirects=False,timeout=9,
        )
        cookies = rst.cookies.get_dict()

        return cookies

    def process_request(self, request, spider):

        if spider.name == 'sougou':
            request.cookies = self.get_random_cookies()
            print(request.cookies, '搜狗更换cookies')
            if 'proxy' not in request.meta:
                self.update_proxy()  # 调用update更新代理，调用的时候对下面的update函数进行判断，如果三
                # 个条件都无法满足则一直使用一样的ip地址..
                # self.current_proxy.start_num +=1
                print('搜狗开始请求数据.....')
                request.meta['proxy'] = self.current_proxy

        else:
            if 'proxy' not in request.meta:
                self.update_proxy()  # 调用update更新代理，调用的时候对下面的update函数进行判断，如果三
                # 个条件都无法满足则一直使用一样的ip地址..
                # self.current_proxy.start_num +=1
                print('开始请求数据.....')
                request.meta['proxy'] = self.current_proxy

            # request.meta['request_num'] = self.current_proxy.start_num

    #             print(request.meta,'meta参数.....')
    #             return None

    def process_response(self, request, response, spider):
        if spider.name in ["tt_id", 'tt_id_', 'tt_id_2','tt_id_3','tt_id_4','tt_id_5','tt_id_6']:

            try:
                gzipfile = gzip.GzipFile('', 'rb', 9, BytesIO(response.body))


                res = gzipfile.read().decode('utf-8')
            except Exception as e:
                print(e,'OS数据的错误......')
                if e:
                    self.current_proxy = None
                    self.update_proxy()
                    request.meta['proxy'] = self.current_proxy
                return request
            if '<html>' not in res:
                if res:
                    print('response正常出现...',res[:88])
                    return response
                else:
                    print('response出现异常更换ip代理',res[:50])
                    self.current_proxy = None
                    self.update_proxy()
                    request.meta['proxy'] = self.current_proxy
                    return request
            else:
                print('出现了<html>')
                self.current_proxy = None
                self.update_proxy()
                request.meta['proxy'] = self.current_proxy
                return request
        if spider.name == 'sougou':
            # gzipfile = gzip.GzipFile('', 'rb', 9, BytesIO(response.body))
            # res = gzipfile.read().decode('utf-8')
            res = str(response.body)

            if 'The URL' in res or '302 Found' in res:
                print(res[:50])
                self.current_proxy = None

                self.update_proxy()

                request.cookies = self.get_random_cookies()
                print(request.cookies,'更换cookies')
                request.meta['proxy'] = self.current_proxy
                return request

            return response
        if  spider.name == 'weibo':
            if response.status == 418:
                print(response.status)
                self.current_proxy = None
                self.update_proxy()
                request.meta['proxy'] = self.current_proxy
                return request
            return response



    def process_exception(self, request, exception, spider):
        print('Got exception:11111111111 %s' % (exception))
        self.current_proxy = None
        self.update_proxy()

        print('%s新代理' % self.current_proxy)
        request.meta['proxy'] = self.current_proxy

    def update_proxy(self):
        self.lock.acquire()
        # 定义了初始变量current_proxy
        print('更新代理之前',self.current_proxy)
        if not self.current_proxy:  # 更换ip这里的条件
            for i in range(1,5):
                time.sleep(0.5)
                proxy_url = self.proxy_url.get("proxy_url2")
                response = requests.get(proxy_url,timeout=10).json()
                # proxy = response.get("proxy")
                ip_data = response.get("data")
                if ip_data:
                    proxy = ip_data[0].get("IP") + ':' + str(response.get("data")[0].get("Port"))
                    self.current_proxy = 'http://' + proxy
                    print('更换新代理ip',self.current_proxy)
                    break

        self.lock.release()




class CeshiDownloaderMiddleware:
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
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
