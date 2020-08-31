from concurrent.futures import ThreadPoolExecutor
import threading
import os
import time


def func1(i):
    print("func1", threading.get_ident())
    time.sleep(0.5)
    return i ** 2


# 回调函数和线程函数运行在相同线程上
def func2(i):
    print("func2", threading.get_ident())
    print(i.result())


if __name__ == '__main__':
    print("主进程", threading.get_ident())
    p = ThreadPoolExecutor(5)
    for i in range(10, 30):
        p.submit(func1, i).add_done_callback(func2)
