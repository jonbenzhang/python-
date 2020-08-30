import socket
import struct
import json
import os

buffer = 1024
port = ("0.0.0.0", 8789)
sk = socket.socket()
sk.connect(port)
head_data = {"file_path": "/home/zhangmeng/Downloads",
             "file_name": "qaz.mp4",
             "data_len": None
             }
path = os.path.join(head_data["file_path"], head_data["file_name"])
file_size = os.path.getsize(path)
head_data["data_len"] = file_size
json_head = json.dumps(head_data)
json_bytes_head = json_head.encode("utf-8")
head_len = struct.pack("i", len(json_bytes_head))
sk.send(head_len)
sk.send(json_bytes_head)
with open(path, "rb") as f:
    while file_size:
        print(file_size)
        if file_size >= buffer:
            content = f.read(buffer)
            file_size -= buffer
        else:
            content = f.read(file_size)
            file_size = 0
        sk.send(content)
sk.close()
