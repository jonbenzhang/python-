# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 下午9:48
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm
# queue是基于线程安全的
import queue


def func1():
    # 设置队列长度为10
    # 队列　先进先出
    q = queue.Queue(10)
    # 队列插入数据，如果队列已满,则阻塞等待
    q.put()
    # 队列取出数据，如果队列为空,则阻塞等待
    q.get()
    # 队列插入数据，如果队列已满,则报错
    q.put_nowait()
    # 队列取出数据，如果队列为空,则报错
    q.get_nowait()


def func2():
    # 设置栈产度为10
    # 设置栈　先进后出
    q = queue.LifoQueue(10)
    # 栈插入数据，如果栈已满,则阻塞等待
    q.put()
    # 栈取出数据，如果栈为空,则阻塞等待
    q.get()
    # 栈插入数据，如果栈已满,则报错
    q.put_nowait()
    # 栈取出数据，如果栈为空,则报错
    q.get_nowait()


def func3():
    # 设置优先级队列
    q = queue.PriorityQueue()
    # 数字越小优先级越高
    # 数字大小相同则按照ascill排序
    q.put((10, "a"))
    q.put((20, "b"))
    q.put((1, "c"))
    q.put((1, "d"))

    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())


if __name__ == '__main__':
    func3()