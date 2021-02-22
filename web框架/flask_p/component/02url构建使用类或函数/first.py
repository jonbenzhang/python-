from flask import Flask

# 蓝图也可以
app = Flask(__name__)

"""
方式1
"""


@app.route("/test", methods=["GET", "POST"])
def test1():
    pass


"""
方式2
"""


def test2():
    pass


app.add_url_rule("/test2", endpoint="test2", view_func=test2,methods=["GET"])
"""
方式3
"""
from flask import views


class Test3(views.MethodView):
    def get(self):
        pass

    def post(self):
        pass


app.add_url_rule("/test3", endpoint="tests3", view_func=Test3.as_view("test3"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
