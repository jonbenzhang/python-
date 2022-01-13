# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.cookies import CookieJar
from scrapy.http import Request
class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['https://dig.chouti.com/']
    #ROBOTSTXT_OBEY = True需要注销掉
    cookie_dict = {}   #其他页面也要cookie，所以定义一个全局的
    def parse(self, response):
        #点赞需要登录才能，所以要携带cookie
        #去响应头中获取cookie,response中获取
        #cookie保存在cookie_jar对象中
        print(response.xpath("//div[@id='dig_lcpage']/a/@href"))
        print('=====')
        # cookie_dict = {}
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)
        #去对象中将cookie解析到字典中
        for k, v in cookie_jar._cookies.items():
            for i, j in v.items():
                for m, n in j.items():
                    self.cookie_dict[m] = n.value
        print("+++++")
        print(self.cookie_dict)

        yield scrapy.Request(
            url="https://dig.chouti.com/login",
            method="POST",
            body="phone=8618588888888&password=88888888&oneMonth=1",
            cookies=self.cookie_dict,
            headers={"content-type":"application/x-www-form-urlencoded; charset=UTF-8"},
            callback=self.check_login

        )

    def check_login(self,response):

        print(response.text)
        print("==============")
        yield scrapy.Request(
            "https://dig.chouti.com/all/hot/recent/1",
            cookies=self.cookie_dict,
            callback=self.index
        )
    def index(self,response):

        div_list = response.xpath("//div[@id='content-list']/div[@class='item']")
        for div in div_list:
            link_id = div.xpath('*/div[@class="part2"]/@share-linkid').extract_first()
            print(link_id)
            #点赞请求
            yield Request(
                url='http://dig.chouti.com/link/vote?linksId=%s' % (link_id,),
                method='POST',
                cookies=self.cookie_dict,
                callback=self.check_result
            )
    def check_result(self,response):
        print(response.text)