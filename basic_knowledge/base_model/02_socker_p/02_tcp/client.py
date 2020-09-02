import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 8995))
while True:
    input_data = input("please input>>")
    # sk.send(bytes(input_data, encoding="utf-8"))
    sk.send(bytes(input_data, encoding="utf-8"))
    if input_data == "bye":
        sk.close()
        break
    ret = sk.recv(1024)


    print(ret.decode("utf-8"))
