import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data = self.request.recv(1024).decode("utf-8")
        print(data)
        self.request.send(b"i'm server")


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 8995

    # 设置allow_reuse_address允许服务器重用地址
    socketserver.TCPServer.allow_reuse_address = True
    # 创建一个server, 将服务地址绑定到127.0.0.1:9999
    server = socketserver.TCPServer((HOST, PORT), MyServer)
    # 让server永远运行下去，除非强制停止程序
    server.serve_forever()
