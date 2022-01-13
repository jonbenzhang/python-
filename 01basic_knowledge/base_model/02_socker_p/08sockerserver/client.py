import socket

sk = socket.socket()

sk.connect(("127.0.0.1", 8995))
# 向server端发送数据
sk.send(b"i'm client")
# 接收server端发来的数据
ret = sk.recv(1024)
# 接收到的为bytes类型，转为str类型
print(ret.decode("utf-8"))
sk.close()
