from multiprocessing import Process, Semaphore
import random
import time


def cesuo(name, sem):
    sem.acquire()
    print("%s进入厕所" % name)
    # 随机生成上厕所的等待时间
    time.sleep(random.randint(1, 5))
    print("%s出了厕所" % name)
    sem.release()


if __name__ == '__main__':
    # 设置只能3个人同时使用资源
    # 在这里的实际意义就是只能有3个人同时在厕所
    sem = Semaphore(3)
    for i in range(30):
        p = Process(target=cesuo, args=(i, sem))
        p.start()
