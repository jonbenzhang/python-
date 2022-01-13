import socket

sk = socket.socket()
# 进行socket 配置
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(("0.0.0.0", 8995))
sk.listen()
print("wait for connect")
while True:
    conn, addr = sk.accept()
    print("have a guest")
    while True:
        ret = conn.recv(1024)
        # bytes --> str
        print(ret.decode("utf-8"))
        input_data = input("input data>>")
        conn.send(bytes(input_data, encoding="utf-8"))
        if input_data == "bye":
            conn.close()
            break


# sk.close()

