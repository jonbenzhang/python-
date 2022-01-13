# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 上午9:29
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm
# 协程使用模块
from greenlet import greenlet


def func1():
    print("func1 start")
    # 切换到协程g2
    g2.switch()
    print("func1 end")


def func2():
    print("func2 start")
    print("func2 end")


# 定义func2的协程,g2
g2 = greenlet(func2)
# 定义func１的协程,g1
g1 = greenlet(func1)
# 切换到协程的g1
g1.switch()
