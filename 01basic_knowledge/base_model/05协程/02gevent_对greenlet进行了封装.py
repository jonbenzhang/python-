# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 上午9:29
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm
# 协程使用模块01first_greenlet.py
from gevent import monkey
import threading

# 需要在这段代码后，倒入有io等待模块，
# 如果没有在这行代码后倒入将无法识别io等待操作
# 协程遇到io操作才会进行切换
monkey.patch_all()
import time
# gevent进行协程调度
import gevent


def func1():
    print("func1 start")
    print(">>func1", threading.current_thread())
    # 不同协程的threading.get_ident()不同，但是这个是应该是在同一线程，为了区分不同协程所以threading.get_ident()不同
    print(threading.get_ident())
    time.sleep(2)
    print("func1 end")


def func2():
    print("func2 start")
    print(">>func2", threading.current_thread())
    # 不同协程的threading.get_ident()不同，但是这个是应该是在同一线程，为了区分不同协程所以threading.get_ident()不同
    print(threading.get_ident())
    time.sleep(2)
    print("func2 end")


def func3():
    print("func3 start")
    print(">>func3", threading.current_thread())
    # 不同协程的threading.get_ident()不同，但是这个是应该是在同一线程，为了区分不同协程所以threading.get_ident()不同
    print(threading.get_ident())
    time.sleep(2)
    print("func2 end")


print(">>主线程", threading.current_thread())

# 定义func１的协程,g1,定义了就会开始执行协程
g1 = gevent.spawn(func1)
# 定义func2的协程,g2
g2 = gevent.spawn(func2)
# 定义func3的协程,g3
g3 = gevent.spawn(func3)
# 等待协程g1运行结束
# 可以看到虽然开启了三个协程，但是仍然只有一个线程存在，说明协程都运行在一个线程上
# print("当前的存活线程数:", threading.active_count())

g2.join()
# 等待协程g2运行结束
g2.join()
g3.join()
