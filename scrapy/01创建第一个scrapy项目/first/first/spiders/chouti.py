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
        # print(response,type(response))
        # print(response.text)
        # 去子孙中找class为link-con的标签,它的子标签中类名包含link-item的
        item_list = response.xpath("//div[@class='link-con']/div[contains(@class,'link-item')]")
        for item in item_list:
            # .//前面加.在当前标签的子孙标签中寻找
            # extract_first() 获取第一个标签
            # 获取text()
            a_tag_text = item.xpath(".//a[contains(@class,'link-title')]/text()").extract_first()
            # strip()去除两边空格
            print(a_tag_text.strip())
            # 获取href属性
            a_tag_href = item.xpath(".//a[contains(@class,'link-title')]/@href").extract_first()
            print(a_tag_href)
