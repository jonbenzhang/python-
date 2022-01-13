# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 下午7:22
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm
import time
import threading


def func1(i):
    time.sleep(0.5)
    # threading.current_thread() 获取到当前的线程
    # threading.get_ident()　获取当前的线程id
    print(i, threading.current_thread(), threading.get_ident())


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=func1, args=(i,))
        t.start()
    # threading.active_count() 获取当前存活的线程数，包括主线程
    print(threading.active_count())
    # threading.enumerate()获取当前存活的所有线程
    print(threading.enumerate())
