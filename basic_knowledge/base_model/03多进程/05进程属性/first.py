from multiprocessing import Process
import time
import os


def func1():
    while True:
        time.sleep(1)
        # 当前进程进程id
        print(os.getpid())
        # 当前进程的父进程id
        print(os.getppid())


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    # 进程名
    print("p1.name", p1.name)
    # 进程id
    print("p1.pid", p1.pid)
    print("p1.is_alive()1", p1.is_alive())
    # 关闭此进程
    p1.terminate()
    # 系统进程关闭需要时间，立即查看可能会发现进程还活着
    print("p1.is_alive()2", p1.is_alive())
    time.sleep(1)
    print("p1.is_alive()3", p1.is_alive())
