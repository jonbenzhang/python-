from flask_old import Flask, Blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
login = Blueprint("login", __name__, url_prefix="/login")
regular = Blueprint("regular", __name__, url_prefix="/regular")
doc = Blueprint("doc", __name__, url_prefix="/doc")


@doc.route("/")
def doc_index():
    return "doc"


@regular.route("/")
def regular_index():
    return "regular"


@login.route("/")
def login_index():
    return "login"


limiter = Limiter(app, default_limits=["1/second"], key_func=get_remote_address)
# regular 蓝图使用默认的使用limiter,因为没有其他
# login 蓝图使用默认的使用新的limiter,60每小时
limiter.limit("60/hour")(login)
# doc 蓝图不见限制
limiter.exempt(doc)

app.register_blueprint(doc)
app.register_blueprint(login)
app.register_blueprint(regular)
