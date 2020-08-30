from multiprocessing import Process, Lock
import time
import json

# dic = {"ticket_num": 2}


def read_ticket():
    with open("a.txt", "r") as f:
        d = json.load(f)
        print(d["ticket_num"])


def buy_ticket(i, lock):
    # 上锁
    lock.acquire()
    with open("a.txt", "r") as f:
        d = json.load(f)
        # print(d["ticket_num"])
    if d["ticket_num"] > 0:
        time.sleep(0.1)
        d["ticket_num"] -= 1
        with open("a.txt", "w")as f:
            json.dump(d, f)
            print("\033[32m%s buy success\033[0m" % i)
    else:
        print("\033[31m%s buy failure\033[0m" % i)
    # 解锁
    lock.release()
if __name__ == '__main__':
    # 进程锁
    lock = Lock()
    for i in range(10):
        p = Process(target=read_ticket)
        p.start()
    for i in range(10):
        p2 = Process(target=buy_ticket,args=(i,lock))
        p2.start()
