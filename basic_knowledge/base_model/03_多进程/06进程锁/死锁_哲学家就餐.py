# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 下午8:10
# @Author  : dataport
# @File    : 01死锁.py
# @Software: PyCharm
import time
from multiprocessing import Process, Lock

noodle_lock = Lock()
fork_lock = Lock()


def eat1(name):
    noodle_lock.acquire()
    print('%s 抢到了面条' % name)
    fork_lock.acquire()
    print('%s 抢到了叉子' % name)
    print('%s 吃面' % name)
    fork_lock.release()
    noodle_lock.release()


def eat2(name):
    fork_lock.acquire()
    print('%s 抢到了叉子' % name)
    time.sleep(1)
    noodle_lock.acquire()
    print('%s 抢到了面条' % name)
    print('%s 吃面' % name)
    noodle_lock.release()
    fork_lock.release()


for name in ['wangguo', 'wenshuo', 'boya']:
    p1 = Process(target=eat1, args=(name,))
    p2 = Process(target=eat2, args=(name,))
    p1.start()
    p2.start()

# 死锁问题
