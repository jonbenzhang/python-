from multiprocessing import Process, Event
import time
import random


def car(name, eve):
    if not eve.is_set():
        print("\033[31m car%s红灯等待中\033[0m" % (name))
        eve.wait()
    print("\033[32m car%s绿灯通过\033[0m" % (name))


def lights(eve):
    while True:
        if eve.is_set():
            print("开启绿灯")
            time.sleep(2)
            eve.clear()
        else:
            print("开启红灯")
            time.sleep(2)
            eve.set()


if __name__ == '__main__':
    eve = Event()
    p1 = Process(target=lights, args=(eve,))
    p1.daemon = True
    p1.start()
    p_list = []
    for i in range(20):
        p2 = Process(target=car, args=(i, eve))
        p_list.append(p2)
        p2.start()
        time.sleep(random.random())
    [p.join()for p in p_list]
