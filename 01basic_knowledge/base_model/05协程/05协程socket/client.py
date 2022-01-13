# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 上午11:48
# @Author  : dataport
# @File    : client.py
# @Software: PyCharm
import socket
import struct

PORT = ("0.0.0.0", 9856)
conn = socket.socket()
conn.connect(PORT)

def func1(conn, addr):
    while True:
        info = input(addr + ">>>").encode("utf-8")
        info_len = len(info)
        info_len_bytes = struct.pack("i", info_len)
        conn.send(info_len_bytes + info)
        if info == b"bye":
            conn.close()
            break
        data_len_bytes = conn.recv(4)
        data_len = struct.unpack('i', data_len_bytes)[0]
        data_bytes = conn.recv(data_len)

        data = data_bytes.decode("utf-8")
        print(data)


if __name__ == '__main__':
    func1(conn, "server")
