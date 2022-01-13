# --*-- encoding:utf8 --*--
from flask_old import Flask, jsonify
from flask_caching import Cache

cache = Cache()


class config():
    # 缓存的存储类型
    CACHE_TYPE = 'redis'
    CACHE_KEY_PREFIX =  "test"  # 存储到redis中的key的前缀
    # 缓存的ip, 端口， 数据库
    CACHE_REDIS_HOST = '172.20.3.29'
    CACHE_REDIS_PORT = 6380
    CACHE_REDIS_DB = 0


app = Flask(__name__)
app.config.from_object(config)
print(app.config)
cache.init_app(app)


@app.route('/', methods=["get"])
@cache.cached(timeout=50)
def test():
    msg = "hello cache"
    print(msg)
    return jsonify(msg=msg)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9003)