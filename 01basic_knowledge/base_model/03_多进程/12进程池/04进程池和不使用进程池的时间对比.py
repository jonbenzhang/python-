from multiprocessing import Pool, Process
import time

# 发现使用进程池要比不使用进程池多花很多时间
# 起一个进程很浪费时间
def func1(n):
    time.sleep(0.1)


if __name__ == '__main__':
    start = time.time()
    p = Pool(8)
    p.map(func1, range(100))
    print(time.time() - start)
    start = time.time()
    process_list = []
    for i in range(100):
        p = Process(target=func1, args=(i,))
        p.start()
        process_list.append(p)
    [p.join() for i in process_list]
    print(time.time() - start)
