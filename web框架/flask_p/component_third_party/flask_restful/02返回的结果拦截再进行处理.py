from flask_old import make_response,Response
from json import dumps
@api.representation('application/json')  # 在视图函数中得到得返回数据，并不立刻直接返回给客户端，而是先经过被representation装饰得函数之后再返回。
def json_representation(data, code, headers=None):
     #  Flask-Restful checks only for flask.Response but flask-login uses werkzeug.wrappers.Response
    if isinstance(data, Response):
        return data
    resp = make_response(dumps(data), code)
    resp.headers.extend(headers or {})
    return resp