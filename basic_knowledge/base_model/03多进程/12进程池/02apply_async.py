from multiprocessing import Pool
import time


def func1(i):
    time.sleep(1)
    return i ** 2


if __name__ == '__main__':
    p = Pool(5)
    result_list = []
    for i in range(20):
        result = p.apply_async(func1, args=(i,))
        result_list.append(result)
    for i in result_list:
        # 进程没有执行完get()会阻塞等待
        print(i.get())
