from flask_old import Flask
from flask_caching import Cache

app = Flask(__name__)
# For more configuration options, check out the documentation
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# 　与app关联,方式2
# cache = Cache(config={'CACHE_TYPE': 'simple'})
# app = Flask(__name__)
# cache.init_app(app)


@app.route("/")
@cache.cached(timeout=50)
def index():
    print("执行index")
    return "are you ok"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8528)