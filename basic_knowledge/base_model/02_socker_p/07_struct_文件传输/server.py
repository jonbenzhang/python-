import socket
import struct
import json

buffer = 1024
port = ("0.0.0.0", 8789)
sk = socket.socket()
sk.bind(port)
sk.listen()
conn, addr = sk.accept()
head_len = struct.unpack("i", conn.recv(4))[0]
print(type(head_len))
bytes_head = conn.recv(head_len)
json_head = bytes_head.decode("utf-8")
head_data = json.loads(json_head)
file_len = head_data["data_len"]
with open(head_data["file_name"], "wb") as file:
    while file_len:
        if file_len > buffer:
            content = conn.recv(buffer)
            file_len -= buffer
        else:
            content = conn.recv(file_len)
            file_len = 0
        file.write(content)
conn.close()
sk.close()
