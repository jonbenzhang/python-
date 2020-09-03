import scrapy


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    # 定向爬虫
    allowed_domains = ['chouti.com']
    # 起始url
    start_urls = ['http://chouti.com/']

    def parse(self, response):
        # response就是　下面倒入的HtmlResponse类的实例化对象
        from scrapy.http.response.html import HtmlResponse
        print(response,type(response))
        print(response.text)
        print(response.xpath())
