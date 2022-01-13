from threading import Thread, Lock
import time

n = 101
b = {"a": 0}


#
# temp = n
# time.sleep(0.2)
# n = temp - 1
# 如果不加锁的话可能会出现，GIL虽然给线程加了锁，但是当线程中运行到temp = n，然后运行time.sleep(0.2)后就会执行其他的线程，造成数据冲突，发生错误

def func1(i, lock):
    # 上锁
    # lock.acquire()
    global b
    for i in range(100000):
        b["a"] = b["a"] + 1
    # temp = n
    # time.sleep(0.2)
    # n = temp - 1
    # 解锁
    # lock.release()


if __name__ == '__main__':
    # 进程锁
    lock = Lock()
    thread_list = []
    for i in range(10000):
        t = Thread(target=func1, args=(i, lock))
        t.start()
        thread_list.append(t)
    for t in thread_list: t.join()
    print(b)
