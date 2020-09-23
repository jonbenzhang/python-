# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 下午5:33
# @Author  : dataport
# @File    : server.py
# @Software: PyCharm
import socket
import select

IP = ("0.0.0.0", 7412)
sk = socket.socket()
# 配置socket 绑定的端口停止可立即使用
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 配置socket为不阻塞
sk.setblocking(False)
sk.bind(IP)
sk.listen()

read_list = [sk]
while True:
    r_list, wi_lst, x_list = select.select(read_list, [], [])
    for i in r_list:
        if i is sk:
            conn, addr = i.accept()
            print(addr, "连接成功")
            read_list.append(conn)
        else:
            # 在后面参数 socket.MSG_DONTWAIT,变为非阻塞recv()
            # 当一个连接没有对方没有发数据，recv会报错
            # 当一个连接断开，recv会接收到b""
            ret = i.recv(1024, socket.MSG_DONTWAIT)
            if ret == b"":
                i.close()
                read_list.remove(i)
                continue
            print(ret)
            i.send(b"goodble")
