# pip install flask-talisman
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

#
# 把请求由http重定向到https
# 重定向仅在app.debug为False发生(Redirects only occur when app.debug is False.)
# 定义方法1
# Talisman(app)
# 定义方法2
talisman = Talisman()
talisman.init_app(
    app,
    force_https=False, # 是否强制所有http连接都转到https
                  )
@app.route("/ping", methods=["GET"])
@talisman(force_https=False)
def ping():
    return "PONG."
