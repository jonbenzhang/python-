# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 上午11:09
# @Author  : dataport
# @File    : 03同步和异步.py
# @Software: PyCharm
from gevent import monkey

monkey.patch_all()
import time
import gevent


def task(i):
    time.sleep(1)
    print("task%s 执行" % i)


def func1():
    # 同步
    for i in range(10):
        task(i)


def func2():
    # 异步
    g_list = []
    for i in range(10):
        g = gevent.spawn(task, i)
        g_list.append(g)
    # for g in g_list: g.join()
    # 等价于上面代码
    gevent.joinall(g_list)



if __name__ == '__main__':
    # func1()
    func2()
