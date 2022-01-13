import scrapy
from first.items import QuotesItem
from scrapy.http import Request


class ChoutiSpider(scrapy.Spider):
    name = 'quotes'
    # 定向爬虫
    allowed_domains = ['quotes.toscrape.com']
    # 起始url
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def start_requests(self):
        """
        类,首先执行start_requests,返回一个可迭代对象
        :return:
        """
        for url in self.start_urls:
            yield Request(url, dont_filter=True)


    def parse(self, response):
        print(response)