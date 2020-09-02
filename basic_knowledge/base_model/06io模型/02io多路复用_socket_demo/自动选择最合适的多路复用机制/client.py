# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 下午6:18
# @Author  : dataport
# @File    : client.py
# @Software: PyCharm
# 客户端
from socket import *

c = socket(AF_INET, SOCK_STREAM)
c.connect(('127.0.0.1', 8088))

while True:
    msg = input('>>: ')
    if not msg: continue
    c.send(msg.encode('utf-8'))
    data = c.recv(1024)
    print(data.decode('utf-8'))
# 基于selectors模块实现聊天
