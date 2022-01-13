from multiprocessing import Process
import time


def func1():
    while True:
        print("i'm alive")
        time.sleep(0.5)


def func2():
    time.sleep(8)
    print("func2 end")


if __name__ == '__main__':
    p1 = Process(target=func1)
    # 设置为守护进程
    # 当主程序代码执行结束后，守护进程自动结束
    # 是代码结束而不是主程序结束，因为如果主程序代码执行完有子进程没有结束，那么守护进程也会结束
    # 1.对主进程来说，运行完毕指的是主进程代码运行完毕
    # 2.对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程统统运行完毕，主线程才算运行完毕
    # 1 主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收）,然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束，
    # 2 主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束
    p1.daemon = True
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    time.sleep(5)
    print("program end>>>>>>")
