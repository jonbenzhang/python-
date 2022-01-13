from multiprocessing import Process
import os
import time


def func1(num):
    print("*" * num)
    time.sleep(3)
    print("%" * num)


if __name__ == '__main__':
    p1 = Process(target=func1, args=(5,))
    p2 = Process(target=func1, args=(1,))
    p1.start()
    p2.start()
    # p1.run()# run会等待进程执行结束后才会继续执行

    p1.join()
    p2.join()
    print("the process end")
