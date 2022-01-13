from flask_old import Flask
from flask_old.signals import _signals

app = Flask(import_name=__name__)

# 自定义信号
xxxxx = _signals.signal('xxxxx')


def func(sender, a):
    print(sender, a)
    print("我是自定义信号")


# 自定义信号中注册函数
xxxxx.connect(func)


@app.route("/")
def index():
    # 触发信号
    xxxxx.send("sb", a="1")
    return 'Index'


if __name__ == '__main__':
    app.run()
