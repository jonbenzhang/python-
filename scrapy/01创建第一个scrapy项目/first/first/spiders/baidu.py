import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    # 定向爬虫
    allowed_domains = ['baidu.com']
    # 起始url
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print(response,type(response))
        # print("*********************")
        # print(type(response))
        # print(response)
        # print("*********************")

