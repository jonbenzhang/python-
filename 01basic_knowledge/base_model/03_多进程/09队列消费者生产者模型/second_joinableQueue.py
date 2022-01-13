from multiprocessing import Process, JoinableQueue
import time
import random


def consumer(name, q):
    while True:
        food = q.get()
        print("%s获取到食物%s" % (name, food))
        time.sleep(random.randint(1, 3))
        q.task_done()


def producer(name, food, q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        f = "%s生产了%s" % (name, food)
        print(f)
        q.put(f)
    q.join()


if __name__ == '__main__':
    q = JoinableQueue(10)
    p1 = Process(target=producer, args=("huofu1", "馒头", q))
    p2 = Process(target=producer, args=("huofu2", "花卷", q))
    c1 = Process(target=consumer, args=("wanshao", q))
    c2 = Process(target=consumer, args=("wenshuo", q))
    c1.daemon = True
    c2.daemon = True
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    p1.join()
    p2.join()
