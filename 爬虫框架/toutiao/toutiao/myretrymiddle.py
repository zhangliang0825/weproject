import logging

from scrapy.downloadermiddlewares.retry import RetryMiddleware

class MyretryMiddleare(RetryMiddleware):
    logger = logging.getLogger(__name__)