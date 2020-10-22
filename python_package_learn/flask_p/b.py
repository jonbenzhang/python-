# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 上午10:35
# @Author  : dataport
# @File    : a.py
# @Software: PyCharm
from flask import Flask, request, session, g
from flask import globals
# RequestContext 中封装了一个　werkzeug 中的 request 对象
from flask.ctx import RequestContext
# werkzeug 中的 request 对象
from flask.wrappers import RequestBase
# from werkzeug.wsgi import
# from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
app1 = Flask("a1")
app2 = Flask("a2")

@app1.route("/")
def a():
    print(request)#LocalProxy.__str_-->  str(LocalProxy get current_object())   --> ctx.request
    print(request.method)
    return "hello"

@app2.route("/tt")
def b():
    return "bb"
ttt = DispatcherMiddleware(
    app1,{
        '/s2':app2
    }
)

if __name__ == '__main__':
    run_simple("0.0.0.0",5000,ttt)
