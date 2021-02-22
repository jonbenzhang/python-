from flask import Flask,request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# 通过请求的remote_address进行速率限制
#
# 默认速率限制为每天200，每小时50，适用于所有路线。
#

#
#
app = Flask(__name__)
limiter = Limiter(
    app,
    # key_func区分一个地方发送的请求的唯一标识使用(get_remote_address为使用地址区分)
    key_func=get_remote_address,
    # 默认速率限制为每天200，每小时50，适用于所有routes。
    default_limits=["200 per day", "50 per hour"]
)


# slow具有明确速率限制装饰器的路由将绕过默认速率限制，并且每天仅允许1个请求。
@app.route("/slow")
@limiter.limit("1 per day")
def slow():
    return ":("


# 该medium路由继承默认限制，并增加了每秒1个请求的修饰限制。
# override_defaults不覆盖默认设置
@app.route("/medium")
@limiter.limit("1/second", override_defaults=False)
def medium():
    return ":|"


# 没加limiter的其他装饰器,使用前面设置的默认速率,限制为每天200，每小时50。
@app.route("/fast")
def fast():
    return ":)"


# 该ping路由将不受任何默认速率限制的约束。
# exempt(豁免)
@app.route("/ping")
@limiter.exempt
def ping():
    return "PONG"

# 装饰的函数返回为true时,就不进行速度限制
@limiter.request_filter
def ip_whitelist():
    # ip为127.0.0.1的不进行limit限制
    return request.remote_addr == "127.0.0.1"

# 使用limit规则的两种方式,
#   方式1:规则使用分号隔开
#   方式2:使用多个装饰器
@app.route("/t1")
@limiter.limit("100/day;10/hour;1/minute")
def t1():
    pass

@app.route("t2")
@limiter.limit("100/day")
@limiter.limit("10/hour")
@limiter.limit("1/minute")
def t2():
    pass


def my_key_func():
    pass

@app.route("...")
# 不使用默认的key_func函数
# 针对此router,使用key_func函数my_key_func
@limiter.limit("100/day", my_key_func)
def my_route():
    pass