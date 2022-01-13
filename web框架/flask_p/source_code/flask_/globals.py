# -*- coding: utf-8 -*-
"""
    flask.globals
    ~~~~~~~~~~~~~

    Defines all the global objects that are proxies to the current
    active context.

    :copyright: 2010 Pallets
    :license: BSD-3-Clause
"""
from functools import partial

from werkzeug.local import LocalProxy
from werkzeug.local import LocalStack
from tag1_0_1.werkzeug.local import LocalProxy
from tag1_0_1.werkzeug.local import LocalStack


_request_ctx_err_msg = """\
Working outside of request context.

This typically means that you attempted to use functionality that needed
an active HTTP request.  Consult the documentation on testing for
information about how to avoid this problem.\
"""
_app_ctx_err_msg = """\
Working outside of application context.

This typically means that you attempted to use functionality that needed
to interface with the current application object in some way. To solve
this, set up an application context with app.app_context().  See the
documentation for more information.\
"""


def _lookup_req_object(name):
    # 获取到该线程或协程的，请求到requestContext对象
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError(_request_ctx_err_msg)
    # 获取到requestContext中的name属性
    return getattr(top, name)


def _lookup_app_object(name):
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    return getattr(top, name)


def _find_app():
    top = _app_ctx_stack.top
    if top is None:
        raise RuntimeError(_app_ctx_err_msg)
    # 拿到当前的app(Flask)
    return top.app


# context locals
# 用来保存RequestContext,每一个线程来了一个请求都会把请求内容保存到RequestContext，然后使用ctx.push()把RequestContext push到栈中
_request_ctx_stack = LocalStack()
# AppContext 封装了当前请求使用的app,和新创建的一个g(每一个请求都新创建一个g)
# 用来保存AppContext,每一个请求的到来,都会使用ctx.push(),中_app_ctx_stack.push(self),把当前请求使用的AppContext,进行压入当前线程中的栈
_app_ctx_stack = LocalStack()
# 获取_app_ctx_stack,最后一次压入栈的app,也就是当前请求使用的app
current_app = LocalProxy(_find_app)
# LocalProxy(函数)传入一个函数
# LocalProxy(函数) 在当前线程或协程中执行函数，获取到函数返回的对象
# _lookup_req_object(name)　返回当前协程中最后一个请求来的RequestContext对象的name属性
# partial(_lookup_req_object, "request")　使用偏函数封装来固定name属性为request, 也就是获取RequestContext中封装的request对象
request = LocalProxy(partial(_lookup_req_object, "request"))
# partial(_lookup_req_object, "session")　使用偏函数封装来固定name属性为session, 也就是获取RequestContext中封装的session对象
# session 为一种特殊的字典类型，为SecureCookieSession(sessions.SecureCookieSession)类
# session["a"] = 1 就是把它放入到了特殊的字典中
session = LocalProxy(partial(_lookup_req_object, "session"))
# _lookup_app_object  在当前线程或协程中执行函数，获取到AppContext 对象(app_ctx)
# partial(_lookup_app_object, "g")　获取到AppContext 对象中的g
# g 每个请求周期都会创建的一个用于在请求周期中传递值的一个容器, 当一次请求前来时可以使用g来进行参数传递，而不用request防止原有参数被覆盖
# 每一个请求一个g,而不像LocalStack每一个线程或协程对应一个
g = LocalProxy(partial(_lookup_app_object, "g"))
