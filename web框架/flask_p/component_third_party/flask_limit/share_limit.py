from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_old import Flask, request

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)


def host_scope(endpoint_name):
    return request.host
# 共享router 的两种使用场景
# 场景1,限制会访问mysql的router的,被访问次数
mysql_limit = limiter.shared_limit("100/hour", scope="mysql")
@app.route("/m1")
@mysql_limit
def m1():
    pass


@app.route("/m2")
@mysql_limit
def m2():
    pass



# 场景2,限制一个ip,对多个router的总的访问次数
host_limit = limiter.shared_limit("100/hour", scope=host_scope)
@app.route("/r1")
@host_limit
def r1():
    pass
@app.route("/r2")
@host_limit
def r2():
    pass
