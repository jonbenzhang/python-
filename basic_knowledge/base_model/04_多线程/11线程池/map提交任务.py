# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 下午10:11
# @Author  : dataport
# @File    : map提交任务.py
# @Software: PyCharm
from concurrent.futures import ThreadPoolExecutor
import time


def func1(i):
    time.sleep(1)
    return i ** 2


if __name__ == '__main__':
    t = ThreadPoolExecutor(5)
    # 返回一个结果的迭代器
    ret = t.map(func1, range(20))
    for i in ret:
        print(i)
