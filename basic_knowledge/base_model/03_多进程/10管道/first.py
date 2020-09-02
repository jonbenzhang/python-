from multiprocessing import Process, Pipe

# 每开启一个进程，通道两端都会增加一个连接
# 如果conn2端的连接有没有关闭的,conn1取完数据就会阻塞住
# 当管道的conn2端的所有连接都关闭时，conn1端的数据都取完（最后就会就报错）
def fun1(conn1, conn2):
    conn2.close()
    while True:
        try:
            msg = conn1.recv()
            print(msg)
        except EOFError:
            conn1.close()
            break



if __name__ == '__main__':
    conn1, conn2 = Pipe()
    Process(target=fun1, args=(conn1, conn2)).start()
    for i in range(20):
        conn2.send("do you eat?")
    conn1.close()
    conn2.close()
