# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 下午4:58
# @Author  : dataport
# @File    : a.py
# @Software: PyCharm
from flask import signals, Flask, render_template
import blinker.base
app = Flask(__name__)


def func(*args, **kwargs):
    print("触发信号", args, kwargs)


signals.request_started.connect(func)


@app.before_first_request
def a1():
    pass


@app.before_first_request
def a2():
    pass


@app.before_request
def a3():
    pass


@app.route("/")
def index():
    return "index"


if __name__ == '__main__':
    app.run(port=3245)
