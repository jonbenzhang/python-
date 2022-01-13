from multiprocessing import Process
import os
import time


class MyProcess(Process):
    def __init__(self, *args):
        super().__init__()
        self.arg = args

    def run(self):
        print("start", self.arg)
        time.sleep(5)
        print("end")


if __name__ == '__main__':
    a = MyProcess(1, 2, 3)
    a.start()
    a.join()
    print("all process end")
