# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 下午5:12
# @Author  : dataport
# @File    : get_p.py
# @Software: PyCharm
import requests

# 修改请求体内容
payload = {'key1': 'value1', 'key2': 'value2'}
# 修改请求头
headers = {'user-agent': 'my-app/0.0.1'}
# 设置请求的cookies
r = requests.get('https://httpbin.org/get', params=payload, headers=headers)
# r = requests.get('https://api.github.com/events')
print(type(r))
print(type(r.text), "请求到的文本内容", r.text)
print(type(r.encoding), "请求到的内容的编码格式", r.encoding)
print(type(r.content), "请求到的内容的字节流响应内容", r.content)
print(type(r.status_code), "请求到的内容的状态码", r.status_code)
print(type(r.headers), "请求到的内容的响应头", r.headers)
print(type(r.json), "请求到的内容的json格式", r.json)
print(type(r.raw), "请求到的内容的socket流内容", r.raw)
print(type(r.cookies), "请求到的内容的cookies", r.cookies)



cookies1 = {"a":1}
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
print(r.cookies)