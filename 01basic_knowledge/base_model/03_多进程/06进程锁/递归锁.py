# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 下午8:14
# @Author  : dataport
# @File    : 递归锁.py
# @Software: PyCharm
# 递归锁可以进行多次加锁，只用进行相对应次数的解锁才会解除递归锁
# 一个线程第一个使用了递归锁上锁，直到这个递归锁的所有加锁都解锁，其余进程才可以使用这个递归锁
import time
from multiprocessing import Process, RLock

lock = RLock()


def eat2(name):
    lock.acquire()
    print('%s 抢到了叉子' % name)
    time.sleep(1)
    lock.acquire()
    print('%s 抢到了面条' % name)
    print('%s 吃面' % name)
    lock.release()
    lock.release()


def eat1(name):
    lock.acquire()
    print('%s 抢到了面条' % name)
    lock.acquire()
    print('%s 抢到了叉子' % name)
    print('%s 吃面' % name)
    lock.release()
    lock.release()


for name in ['wangguo', 'wenshuo', 'boya']:
    p1 = Process(target=eat1, args=(name,))
    p2 = Process(target=eat2, args=(name,))
    p1.start()
    p2.start()

# 递归锁解决死锁问题
