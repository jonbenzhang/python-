"""
直接使用scrapy 中的xpath解析模块
"""
from scrapy.http import HtmlResponse
from scrapy.selector import Selector

html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>
"""
# 方式一
response = HtmlResponse(url="https://www.baidu.com", body=html_doc, encoding="utf-8")
response.xpath()



# 方式２
