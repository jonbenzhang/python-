from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, arg1,arg2):
        super().__init__()
        self.arg1 = arg1

    def run(self):
        print("start", self.arg1)
        time.sleep(5)
        print("end")


if __name__ == '__main__':
    thread_list = []
    for i in range(10):
        a = MyThread(i, 2)
        a.start()
        thread_list.append(a)
    [p.join() for p in thread_list]
    print("所有线程结束")
