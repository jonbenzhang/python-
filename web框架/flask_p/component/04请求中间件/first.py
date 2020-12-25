from ...source_code.flask import Flask

app = Flask(__name__)


# 返回值会被忽略
@app.teardown_request
def a(e):
    # e 为捕获到的异常的值，自己抛出的异常经常获取到为None具体原理,以后分析
    print("ddd")
    return "返回会被忽略"


@app.handle_exception(ImportError)
def b(e):
    # flask_restful组件中抛出的异常无法捕捉
    # 判断捕获到的异常的类型
    isinstance(e, ImportError)
    # 返回值，会成为请求的返回结果
    return {}
