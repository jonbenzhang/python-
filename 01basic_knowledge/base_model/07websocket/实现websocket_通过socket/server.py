# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 上午10:22
# @Author  : dataport
# @File    : server.py
# @Software: PyCharm
import socket
import base64
import hashlib


def get_headers(data):
    """
    将请求头格式化成字典
    :param data:
    :return:
    """
    header_dict = {}
    data = str(data, encoding='utf-8')
    header, body = data.split('\r\n\r\n', 1)
    header_list = header.split('\r\n')
    for i in range(0, len(header_list)):
        if i == 0:
            if len(header_list[i].split(' ')) == 3:
                header_dict['method'], header_dict['url'], header_dict['protocol'] = header_list[i].split(' ')
        else:
            k, v = header_list[i].split(':', 1)
            header_dict[k] = v.strip()
    return header_dict


def send_msg(msg_bytes):
    """
    WebSocket服务端向客户端发送消息
    :param conn: 客户端连接到服务器端的socket对象,即： conn,address = socket.accept()
    :param msg_bytes: 向客户端发送的字节
    :return:
    """
    import struct

    token = b"\x81"
    length = len(msg_bytes)
    if length < 126:
        token += struct.pack("B", length)
    elif length <= 0xFFFF:
        token += struct.pack("!BH", 126, length)
    else:
        token += struct.pack("!BQ", 127, length)

    msg = token + msg_bytes
    return msg


def deciphering(info):
    """
    对获取到的websocket数据进行解密
    :param info:
    :return:
    """
    payload_len = info[1] & 127
    if payload_len == 127:
        extend_payload_len = info[2:10]
        mask = info[10:14]
        decoded = info[14:]
    elif payload_len == 126:
        extend_payload_len = info[2:4]
        mask = info[4:8]
        decoded = info[8:]
    else:
        extend_payload_len = None
        mask = info[2:6]
        decoded = info[6:]

    bytes_list = bytearray()
    for i in range(len(decoded)):
        chunk = decoded[i] ^ mask[i % 4]
        bytes_list.append(chunk)
    body = str(bytes_list, encoding='utf-8')
    return body


IP = ("0.0.0.0", 8008)
sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(IP)
sk.listen()
while True:
    # 1.等待websocket前来连接
    conn, addr = sk.accept()
    print("连接%s到来" % str(addr))
    # 2.接收消息
    msg = conn.recv(4096)
    print(repr(msg.decode("utf-8")))
    print(msg.decode("utf-8"))
    msg_dict = get_headers(msg)
    print("获取到验证消息", msg_dict["Sec-WebSocket-Key"])
    # 对数据进行加密
    value = msg_dict['Sec-WebSocket-Key'] + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
    # print(ac,type(ac))
    # 4. 将加密后的结果返回给
    response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
                   "Upgrade:websocket\r\n" \
                   "Connection: Upgrade\r\n" \
                   "Sec-WebSocket-Accept: %s\r\n" \
                   "WebSocket-Location: ws://0.0.0.0:8008\r\n\r\n"
    response = response_tpl % (ac.decode('utf-8'),)
    print(repr(response))
    print(response)
    conn.send(response.encode('utf-8'))
    # 5.连接成功等待接收消息
    while True:
        msg = conn.recv(1024)
        msg_str = deciphering(msg)
        print(msg_str)
        conn.send(send_msg(msg_str.encode("utf-8")))