import scrapy
from first.items import QuotesItem

class ChoutiSpider(scrapy.Spider):
    name = 'quotes'
    # 定向爬虫
    # allowed_domains = ['quotes.toscrape.com/']
    allowed_domains = ['quotes.toscrape.com']
    # 起始url
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        div_list = response.xpath("/html/body/div/div[2]/div[1]/div[@class='quote']")
        for div in div_list:
            # .//前面加.在当前标签的子孙标签中寻找
            # extract_first() 获取第一个标签
            # 获取text()
            div_tag_text = div.xpath("./span[@class='text']/text()").extract_first()
            # strip()去除两边空格
            yield QuotesItem(content=div_tag_text.strip())
        # 第一页只会获取到一个
        # 第二页开始，都会获取到两个标签，一个上一页，一个下一页
        next_page_url = response.xpath("/html/body/div/div[2]/div[1]/nav/ul/li/a/@href").extract()
        print(next_page_url)
        # 进行翻页
        for next_page_url in next_page_url:
            from scrapy.http import Request
            url = "http://quotes.toscrape.com" + next_page_url
            print(url)
            # 爬取过的网页不会再次进行爬取
            # dont_filter=True 设置为True不遵守去重规则，默认为False遵守去重规则
            yield Request(url=url, callback=self.parse)
