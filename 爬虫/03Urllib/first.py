# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 下午4:13
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm
from urllib import request

# urlopen默认为get请求，如有data数据传入自动变为post请求
# url 请求的网址
# data post请求传递数据
# timeout 设置超时时间
# urllib.request.urlopen(url, data=None, [timeout, ]*)
response = request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))





url1 = "http://cskaoyan.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LlZ2d&inajax=1"
# 修改请求头中的信息，来欺骗服务器
# urllib.request.Request(url, data=None, headers={}, method=None)
from urllib import request, parse
import ssl
context = ssl._create_unverified_context()
# 请求头伪装
headers = {
    # 假装自己是浏览器
    'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
# post请求参数
dict = {
    'user_name': '741852963@yahu',
    'password': '645a9966329b6c65df23d2809c7e4e2ed',
}
# 参数转为byte类型
data = bytes(parse.urlencode(dict), "utf-8")
request.Request(url1)

req = request.Request(url1, data=data, headers=headers, method='POST')
response = request.urlopen(req,context=context)
print(response.read().decode())
# print(response.read().decode('utf-8'))