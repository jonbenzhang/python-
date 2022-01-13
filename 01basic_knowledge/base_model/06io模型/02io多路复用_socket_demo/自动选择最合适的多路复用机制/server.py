# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 下午6:17
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm
# 服务端
import socket
import selectors

sel = selectors.DefaultSelector()


def accept(sk, mask):
    conn, addr = sk.accept()
    # selectors.EVENT_READ指定监听一个读事件
    # 相当于网select的读列表里append了一个conn
    # 并且绑定了一个回调函数accept
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    try:
        data = conn.recv(1024)
        if not data:
            print('closing', conn)
            # 取消对conn的监听
            sel.unregister(conn)
            conn.close()
            return
        conn.send(data.upper() + b'_SB')
    except Exception:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', 8088))
sk.listen(5)
sk.setblocking(False)  # 设置socket的接口为非阻塞
# 相当于网select的读列表里append了一个socket对象sk,并且绑定了一个回调函数accept
sel.register(sk, selectors.EVENT_READ, accept)

while True:
    events = sel.select()  # 检测是否有完成wait data的，也就是有可读对象
    for sel_obj, mask in events:
        callback = sel_obj.data  # 拿到注册的回调函数，callback=accpet
        # sel_obj.fileobj 是传入的对象，这个程序中有sk和conn
        # make要监听的读写方式等，这里为selectors.EVENT_READ，
        callback(sel_obj.fileobj, mask)  # accpet(sk,1)
