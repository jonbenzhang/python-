from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def run(self):
        print("start", self.arg)
        time.sleep(5)
        print("end")


if __name__ == '__main__':
    a = MyThread(1)
    a.start()
    # 等待线程执行结束否则阻塞
    a.join()
    print("所有线程结束")
