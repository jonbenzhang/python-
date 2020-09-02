# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 下午3:46
# @Author  : dataport
# @File    : server.py
# @Software: PyCharm
import socket

IP = ("0.0.0.0", 7412)
sk = socket.socket()
# 配置socket 绑定的端口停止可立即使用
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 配置socket为不阻塞
sk.setblocking(False)
sk.bind(IP)
sk.listen()

conn_list = []
conn_del_list = []
while True:
    try:
        conn, addr = sk.accept()
        conn_list.append(conn)
        print(addr, "连接成功")
    except BlockingIOError:
        for con in conn_list:
            try:
                # 在后面参数 socket.MSG_DONTWAIT,变为非阻塞recv()
                # 当一个连接没有对方没有发数据，recv会报错
                # 当一个连接断开，recv会接收到b""
                data = con.recv(1024, socket.MSG_DONTWAIT)
                if data == b"":
                    conn_del_list.append(con)
                    continue
                print(data)
            except BlockingIOError:
                pass
        for con in conn_del_list:
            conn_list.remove(con)
        conn_del_list.clear()
