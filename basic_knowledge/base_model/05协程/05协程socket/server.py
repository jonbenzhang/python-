# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 上午11:48
# @Author  : dataport
# @File    : server.py
# @Software: PyCharm
import socket
import struct
import gevent

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(("0.0.0.0", 9856))
sk.listen()


def func1(conn, addr):
    print(addr)
    while True:
        data_len_bytes = conn.recv(4)
        data_len = struct.unpack('i', data_len_bytes)[0]
        data_bytes = conn.recv(data_len)
        data = data_bytes.decode("utf-8")
        print(data)
        if data == "bye":
            conn.close()
            break
        # info = input(addr + ">>>")
        info = "你好"
        info = info.encode("utf-8")
        info_len = len(info)
        info_len_bytes = struct.pack("i", info_len)
        conn.send(info_len_bytes + info)


while True:
    conn, addr = sk.accept()
    print("llll")
    g = gevent.spawn(func1, conn, addr)
    g.join()
