from multiprocessing import Pool
import time


def func1(i):
    time.sleep(1)
    return i ** 2


if __name__ == '__main__':
    p = Pool(5)
    for i in range(20):
        result = p.apply(func1, args=(i,))
        print(result)

