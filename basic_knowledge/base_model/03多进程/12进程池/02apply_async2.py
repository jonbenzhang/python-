from multiprocessing import Pool
import time


def func1(i):
    time.sleep(1)
    print(i)


if __name__ == '__main__':
    p = Pool(5)
    result_list = []
    for i in range(20):
        p.apply_async(func1, args=(i,))
    p.close()
    p.join()
