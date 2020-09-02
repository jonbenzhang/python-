import socket

sk = socket.socket()
# 进行socket 配置
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 配置监听ip和　端口
sk.bind(("0.0.0.0", 8995))
# 开始进行监听
sk.listen()
print("等待连接")
# conn 获取到的连接
# addr 连接的client端的地址
conn, addr = sk.accept()
print(conn)
print(addr)
# 接收client端发来的数据
ret = conn.recv(1024)
# bytes --> str
print(ret.decode("utf-8"))
# 向client发送数据
conn.send(b"i'm server")
conn.close()
sk.close()
