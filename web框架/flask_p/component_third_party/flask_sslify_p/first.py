from flask_sslify import SSLify
from flask_old import Flask

app = Flask(__name__)

# flask_sslify已经不再维护，官方建议使用flask-talisman
# 把请求由http重定向到https
# 重定向仅在app.debug为False发生
# skips :以skips列表中字符串开头的path,不进行重定向

SSLify(app, skips=['ping'])
