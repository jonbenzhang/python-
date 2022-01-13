import scrapy
from first.items import QuotesItem
from scrapy.http import Request
class ChoutiSpider(scrapy.Spider):
    name = 'quotes2'
    # 定向爬虫
    # allowed_domains = ['quotes.toscrape.com/']
    allowed_domains = ['quotes.toscrape.com']
    # 起始url
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        import os
        # 使用代理的方式1
        os.environ["HTTPS_PROXY"] = "http://root:zhangmeng@10.20.2.2:9999"
        os.environ["HTTP_PROXY"] = "10.20.2.2:9999"
        # 使用代理的方式2
        # 写在meta中
        yield Request(url="www.baidu.com",callback=self.parse,meta={"proxy":"http://root:zhangmeng@10.20.2.2:9999"})