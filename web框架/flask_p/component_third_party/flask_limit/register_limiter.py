from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_old import Flask
# 定义flask_limiter到flask上
# 定义方式1
app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)
# Deferred app initialization using init_app
# 定义方式2
limiter = Limiter(key_func=get_remote_address)
limiter.init_app(app)