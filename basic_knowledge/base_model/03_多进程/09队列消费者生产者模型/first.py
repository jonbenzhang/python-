from multiprocessing import Process, Queue
import time
import random


def consumer(name, q):
    while True:
        food = q.get()
        if food is None:
            print("%s获取到空停止" % name)
            break
        print("%s获取到食物%s" % (name, food))
        time.sleep(random.randint(1, 3))


def producer(name, food, q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        f = "%s生产了%s" % (name, food)
        print(f)
        q.put(f)


if __name__ == '__main__':
    q = Queue(10)
    p1 = Process(target=producer, args=("huofu1", "馒头", q))
    p2 = Process(target=producer, args=("huofu2", "花卷", q))
    c1 = Process(target=consumer, args=("wanshao", q))
    c2 = Process(target=consumer, args=("wenshuo", q))
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    q.put(None)
    q.put(None)
