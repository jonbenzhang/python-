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
    process_list = []
    for i in range(10):
        a = MyProcess(1, 2, 3)
        a.start()
        process_list.append(a)
    [p.join() for p in process_list]
    print("all process end")
