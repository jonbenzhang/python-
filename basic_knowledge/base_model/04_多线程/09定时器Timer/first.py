# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 下午9:29
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm
from threading import Timer


def func1(a):
    print(a)
    print("i'm func1")


# 延迟2秒开启一个线程
t = Timer(2, func1, args=("aa",))
t.start()
