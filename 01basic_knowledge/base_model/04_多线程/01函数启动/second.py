from threading import Thread
import time


def func1(num):
    print("*" * num)
    time.sleep(3)
    print("%" * num)


if __name__ == '__main__':
    pro_list = []
    for i in range(10):
        p = Thread(target=func1, args=(i,))
        p.start()
        pro_list.append(p)
    # 等待所有的线程执行完毕
    [p.join() for p in pro_list]
    print("the process end")
