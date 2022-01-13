import threading


# run1第二道锁
def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num


# run2第三道锁
def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2


# run3相当于第一道锁
def run3():
    # 获取一把锁
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    # 释放一把锁
    lock.release()
    print(res, res2)


# 生成两个变量
num, num2 = 0, 0

# 生成递归锁实例
lock = threading.RLock()

# 循环开启10个线程
for i in range(10):
    t = threading.Thread(target=run3)
    t.start()

# 如过大于1个线程就成立
while threading.active_count() != 1:

    # 打印当前还有多少个线程
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)
