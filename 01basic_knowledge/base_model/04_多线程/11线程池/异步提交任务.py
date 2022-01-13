# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 下午10:11
# @Author  : dataport
# @File    : 异步提交任务.py
# @Software: PyCharm
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def func1(i):
    time.sleep(1)
    return i ** 2


if __name__ == '__main__':
    t = ThreadPoolExecutor(5)  # 一般不超过cpu数*5
    result_list = []
    for i in range(20):
        result = t.submit(func1, i)
        result_list.append(result)
    t.shutdown(wait=False)
    # wait = True，等待池内所有任务执行完毕回收完资源后才继续
    # wait = False，立即返回，并不会等待池内的任务执行完毕
    for i in result_list:
        # 如果线程没有执行完result()会阻塞等待
        print(i.result())
