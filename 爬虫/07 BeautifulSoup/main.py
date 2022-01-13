# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 上午11:25
# @Author  : dataport
# @File    : main.py
# @Software: PyCharm
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
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')
print(soup.title.string)
