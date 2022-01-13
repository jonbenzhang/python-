from multiprocessing import Pipe, Process, Lock
import time
import random

# 管道不是基于进程安全的多进程读取或写入需要加锁
# 多进程优先使用队列
def consumer(name, conn1, conn2,lock):
    while True:
        try:
            conn1.close()
            lock.acquire()
            time.sleep(random.random())
            food = conn2.recv()
            lock.release()
            print("%s获取到食物%s" % (name, food))
        except EOFError:
            print(name)
            conn2.close()
            break

def producer(name, food, conn1, conn2, lock):
    conn2.close()
    for i in range(10):
        f = "%s生产了%s" % (name, food)
        print(f)
        lock.acquire()
        conn1.send(f)
        time.sleep(random.random())
        lock.release()
    conn1.close()


if __name__ == '__main__':
    lock = Lock()
    lock2 = Lock()
    conn1, conn2 = Pipe()
    p1 = Process(target=producer, args=("huofu1", "馒头", conn1, conn2, lock2))
    p2 = Process(target=producer, args=("huofu2", "花卷", conn1, conn2, lock2))
    c1 = Process(target=consumer, args=("wanshao", conn1, conn2, lock))
    c2 = Process(target=consumer, args=("wenshuo", conn1, conn2, lock))
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    conn1.close()
    conn2.close()

