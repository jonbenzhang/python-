from multiprocessing import Manager, Process, Lock


# Manager中的数据，基于进程是不安全的需要加锁
def work(d, lock):
    with lock:  # 不加锁而操作共享的数据,肯定会出现数据错乱
        d['count'] -= 1


if __name__ == '__main__':
    lock = Lock()
    with Manager() as m:
        dic = m.dict({'count': 100})
        p_l = []
        for i in range(100):
            p = Process(target=work, args=(dic, lock))
            p_l.append(p)
            p.start()
        for p in p_l:
            p.join()
        print(dic)
# Manager例子
