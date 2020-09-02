from multiprocessing import Pool
import os
import time


def func1(i):
    print("func1",os.getpid())
    time.sleep(0.5)
    return i ** 2

# 回调函数运行在主进程上
def func2(i):
    print("func2",os.getpid())
    print(i)


if __name__ == '__main__':
    print("主进程",os.getpid())
    p = Pool(5)
    for i in range(10, 30):
        p.apply_async(func1, args=(i,), callback=func2)
    p.close()
    p.join()
