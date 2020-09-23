# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 下午5:41
# @Author  : dataport
# @File    : client.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 下午3:47
# @Author  : dataport
# @File    : client.py
# @Software: PyCharm
import socket
from threading import Thread
import time
IP = ("0.0.0.0", 7412)


def func1(name):
    conn = socket.socket()
    conn.connect(IP)
    info = name.encode("utf-8") + b"hello"
    print(info)
    conn.send(info)
    time.sleep(3)
    print(conn.recv(1024).decode("utf-8"))
    # info = input(addr + ">>>").encode("utf-8")


if __name__ == '__main__':
    t_list = []
    for i in range(10):
        t = Thread(target=func1, args=(str(i),))
        t.start()
        t_list.append(t)
    for i in t_list:
        i.join()

