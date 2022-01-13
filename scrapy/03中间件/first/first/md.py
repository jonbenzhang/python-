"""
下载中间件
执行顺序
Md1.process_request
Md2.process_request
Md2.process_response
Md1.process_response
Sd1.input
Sd2.input
<200 http://quotes.toscrape.com/page/1/>
Sd1.output
Sd2.output
"""
# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.http import Request
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
"""

"""



class Md1:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    @classmethod
    def from_crawler(cls, crawler):
        # 如果有from_crawler方法则调用from_crawler方法来进行实例化对象
        # This method is used by Scrapy to create your spiders.
        s = cls()
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
        print("Md1.process_request")

        # 第一种　返回HtmlResponse
        # 自己进行下载
        #  这里返回一个HtmlResponse对象，就不会继续执行后面的Md2.process_request了
        # 就不会把request传入到下载器进行下载了
        # import requests
        # result = requests.get(request.url)
        # return HtmlResponse(url=request.url, status=200, headers=None, body=result.content)
        # 第二种返回Request,返回去处理这个Request
        # return Request(url="http://www.baidu.cpm")
        # 第三种抛出异常
        # 直接哦停止处理这个请求
        # from scrapy.exceptions import IgnoreRequest
        # raise IgnoreRequest
        # 第四种对请求进行加工
        # 比如每次在请求头中加固定的参数

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        # 查看Md1.process_request中的几种返回，process_response实现的效果类似
        print("Md1.process_response")
        return response


class Md2:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        print("Md2.process_request")

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        print("Md2.process_response")
        return response


