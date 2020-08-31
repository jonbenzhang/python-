from threading import Thread, Event
import time
import random


def connect_db(e):
    count = 3
    while count:
        e.wait(1)
        if e.is_set() is True:
            print("连接数据库成功")
            break
        else:
            count -= 1
            print("连接数据库失败")
    # 当count为0时会执行else
    else:
        raise TimeoutError


def connect_test(e):
    time.sleep(random.randint(0, 2))
    e.set()


if __name__ == '__main__':
    e = Event()
    t1 = Thread(target=connect_db, args=(e,))
    t2 = Thread(target=connect_test, args=(e,))
    t1.start()
    t2.start()

