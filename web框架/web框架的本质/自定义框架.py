import socket
from jinja2 import Template

IP = ("0.0.0.0", 8080)


def a(request):
    return b"this is a"


def b(request):
    import os
    path = os.path.dirname(__file__)
    path = os.path.join(path, "template/b.html")
    with open(path, "rb") as f:
        data = f.read()
        return data


def c(request):
    import os
    import time
    path = os.path.dirname(__file__)
    path = os.path.join(path, "template/c.html")
    with open(path, "r") as f:
        data = f.read()
        data = data.replace("{{time}}", str(time.ctime()))
        return data.encode("utf-8")


def d(request):
    import os
    import time
    path = os.path.dirname(__file__)
    path = os.path.join(path, "template/d.html")
    with open(path, "r") as f:
        data = f.read()
        template = Template(data)
        data = template.render(time=time.ctime())
        return data.encode("utf-8")


routers = {
    "/a": a,
    "/b": b,
    "/c": c,
    "/d": d,
}


def router(request):
    print(request.url)
    print(request.url.split("?")[0])
    for url in routers:
        if url == request.url.split("?")[0]:
            return routers[url](request)
    return b"404"


class Request:
    pass


class Header:
    pass


def run():
    sk = socket.socket()
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind(IP)
    sk.listen()
    while True:
        conn, addr = sk.accept()
        print("conn *******************")
        request = Request()
        request_bytes = conn.recv(8096)
        request_str = str(request_bytes, encoding="utf-8")
        if request_str == "":
            conn.close()
            continue
        print(repr(request_str))
        request_header_list = request_str.split("\r\n\r\n")[0].split("\r\n")
        request.data = request_str.split("\r\n\r\n")[1]
        request.method = request_header_list[0].split(" ")[0]
        request.url = request_header_list[0].split(" ")[1]
        header = Header()
        for i in request_header_list[1:]:
            key, value = i.split(": ")
            header.key = value
        request.header = header
        response = router(request)
        print(response)
        conn.send(b"HTTP/1.1 200 OK \r\n\r\n")
        conn.send(response)
        conn.close()
        # print(request)
        # print(repr(request_str))


if __name__ == '__main__':
    run()
