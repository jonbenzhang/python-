# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 下午5:05
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm
import requests
# get请求,设置超时
r = requests.get("https://api.github.com/events",timeout=0.1)
# post 请求
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
# 各种请求的实现方式
r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')


