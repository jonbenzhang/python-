from flask_restful import abort, Resource, Api
from flask import Blueprint

"""
下面是通过flask_restful定义接口，定义的接口在蓝图上
"""


class Person(Resource):
    def get(self):
        return "这是get请求"

    def post(self):
        return "这是post请求"

    def delete(self):
        return "这是delete请求"

    def put(self):
        return "这是put请求"


# 定义蓝图
routes = Blueprint('gongwei', __name__)
# 把api注册在蓝图上
api = Api(routes)
# 还可以使用,api.init_app把连接在蓝图上
api.init_app(routes)

"""
定义在flask app上
"""
from flask import Flask

app = Flask(__name__)
# 把api连接在app上
api = Api(app)
# 还可以使用,api.init_app把连接在app上
api.init_app(routes)

"""
添加api接口
"""
api.add_resource(Person, "/PersonalHealthRecord")

"""
停止返回错误
"""
from flask_restful import abort

# 400为状态码,其余的key-value会通过json的形式返回
# message不为固定,可自定义变量
# 这个abort只能在通过flask_restful.Api()定义的接口上使用，因为flask_restful做了处理
abort(400, message="错误信息", b="自定义")
"""
{
    "message": "错误信息",
    "b":"自定义"
}
"""
