# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 下午9:12
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm


# con.notify(num)和con.wait()必须在con.acquire()和con.release()之间进行使用

from threading import Condition, Thread


def func1(con, i):
    print("start%s" % i)
    # 加线程锁
    con.acquire()
    print("go%s" % i)
    # 线程挂起等待
    con.wait()
    print("在线程%s中" % i)
    # 释放程锁
    con.release()


con = Condition()
for i in range(15):
    Thread(target=func1, args=(con, i)).start()

while True:
    num = int(input(">>>"))
    con.acquire()
    # 　通知num个线程，停止挂起，继续运行
    con.notify(num)
    # 通知所有的线程，停止挂起，继续运行
    # con.notifyAll()
    con.release()
