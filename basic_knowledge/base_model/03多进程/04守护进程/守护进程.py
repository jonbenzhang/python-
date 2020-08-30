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
    p1.daemon = True
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    time.sleep(5)
    print("program end>>>>>>")
