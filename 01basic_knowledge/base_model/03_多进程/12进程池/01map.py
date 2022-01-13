from multiprocessing import Pool
import time

def func1(i):
    time.sleep(1)
    print(i)
    return i ** 2


if __name__ == '__main__':
    p = Pool(5)
    p.map(func1,range(20))
    # print(ret)
