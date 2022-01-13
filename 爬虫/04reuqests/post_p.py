# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 下午5:47
# @Author  : dataport
# @File    : post_p.py
# @Software: PyCharm
import requests


def post_args_two():
    payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
    r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
    payload_dict = {'key1': ['value1', 'value2']}
    r2 = requests.post('https://httpbin.org/post', data=payload_dict)
    # 上面两种方案都会实现如下效果
    # {  ...  "form": {    "key1": [      "value1",      "value2"    ]  },  ...}
    print(r1.text)
    print(r1.text == r2.text)


# post 使用json参数
def post_json():
    url = 'https://httpbin.org/post'
    payload = {'some': 'data'}
    r = requests.post(url, json=payload)
    print(r.text)


# post上传文件
def post_file():
    url = 'https://httpbin.org/post'
    files = {'file': open('a.txt', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)

# 获取cookie
def post_cookie():
    url = 'http://example.com/some/cookie/setting/url'
    r = requests.get(url)
    print(r.cookies)
    # print(r.cookies['example_cookie_name'])
if __name__ == '__main__':
    post_cookie()
