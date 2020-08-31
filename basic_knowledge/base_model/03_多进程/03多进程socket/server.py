import socket
from multiprocessing import Process


def func1(conn):
    while True:
        ret = conn.recv(1024)
        # bytes --> str
        print(ret.decode("utf-8"))
        if ret.decode("utf-8") == "bye":
            break
        input_data = "input word"
        conn.send(bytes(input_data, encoding="utf-8"))
        if input_data == "bye":
            conn.close()
            break


sk = socket.socket()
# 进行socket 配置
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(("0.0.0.0", 8995))
sk.listen()
print("wait for connect")
while True:
    conn, addr = sk.accept()
    print("have a guest")
    p = Process(target=func1,args=(conn,))
    p.start()

# sk.close()
