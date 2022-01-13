# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 下午4:58
# @Author  : dataport
# @File    : a.py
# @Software: PyCharm
"""
flask内置信号的使用
"""
from flask_old import signals, Flask
# import blinker.base

app = Flask(__name__)

# 内置
def func(*args, **kwargs):
    """
    自定义函数,当有信号时候进行触发
    """
    print("触发信号", args, kwargs)


# request_started = _signals.signal('request-started')                # 请求到来前执行
# request_finished = _signals.signal('request-finished')              # 请求结束后执行
#
# before_render_template = _signals.signal('before-render-template')  # 模板渲染前执行
# template_rendered = _signals.signal('template-rendered')            # 模板渲染后执行
#
# got_request_exception = _signals.signal('got-request-exception')    # 请求执行出现异常时执行
#
# request_tearing_down = _signals.signal('request-tearing-down')      # 请求执行完毕后自动执行（无论成功与否）
# appcontext_tearing_down = _signals.signal('appcontext-tearing-down')# 请求上下文执行完毕后自动执行（无论成功与否）
#
# appcontext_pushed = _signals.signal('appcontext-pushed')            # 请求上下文push时执行
# appcontext_popped = _signals.signal('appcontext-popped')            # 请求上下文pop时执行
# message_flashed = _signals.signal('message-flashed')                # 调用flask在其中添加数据时，自动触发

# 把内置信号request_started,绑定函数func,当触发信号的时候,就会调用func函数
signals.request_started.connect(func)
# 把内置信号request_finished,绑定函数func,当触发信号的时候,就会调用func函数
signals.request_finished.connect(func)


@app.route("/")
def index():
    return "index"


if __name__ == '__main__':
    app.run(port=3245)

