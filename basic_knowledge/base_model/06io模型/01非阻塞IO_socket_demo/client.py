# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 下午3:47
# @Author  : dataport
# @File    : client.py
# @Software: PyCharm
import socket
import gevent

IP = ("0.0.0.0", 7412)



def func1( name):
    conn = socket.socket()
    conn.connect(IP)
    info = name.encode("utf-8") + b"hello"
    print(info)
    conn.send(info)
    # info = input(addr + ">>>").encode("utf-8")


if __name__ == '__main__':
    g_list = []
    for i in range(20):
        g = gevent.spawn(func1, str(i))
        g_list.append(g)
    gevent.joinall(g_list)
