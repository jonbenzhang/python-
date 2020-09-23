# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 上午10:54
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm
from threading import Thread
import os
import time


def func1(num):
    print("*" * num)
    time.sleep(3)
    print("%" * num)


if __name__ == '__main__':
    p1 = Thread(target=func1, args=(5,))
    p2 = Thread(target=func1, args=(1,))
    p1.start()
    p2.start()
    # 等待线程p1执行完毕
    p1.join()
    # 等待线程p2执行完毕
    p2.join()
    print("the process end")
