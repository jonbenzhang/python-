# -*- coding: utf-8 -*-
# @Time    : 2020/9/2 上午9:46
# @Author  : dataport
# @File    : first.py
# @Software: PyCharm
from flask_old import Flask, render_template, request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/message")
def message():
    client = request.environ.get("wsgi.websocket")
    if not client:
        return "您使用的不是websocket协议"
    while True:
        message = client.receive()
        print(message)
        client.send(message)



if __name__ == '__main__':
    # 通过这样启动使得flask支持websocket
    http_server = WSGIServer(('0.0.0.0', 9632), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
