# --*-- encoding:utf8 --*--
from flask_old import Flask, jsonify
from flask_caching import Cache

app = Flask(__name__)

cache1 = Cache()
cache2 = Cache()
cache1.init_app(app, config={
    'CACHE_TYPE': 'redis',  # 设置使用缓存的类型,为redis
    "CACHE_KEY_PREFIX": "test",  # 存储到redis中的key的前缀
    'CACHE_REDIS_HOST': '172.20.3.29',  # 设置host
    'CACHE_REDIS_PORT': '6380',  # 设置port
    'CACHE_REDIS_DB': 0,  # 设置选择的redis库
    # 'CACHE_REDIS_URL':"redis://172.20.3.29:6380/0"# 可以使用url
    'CACHE_OPTIONS': {},  # CACHE_OPTIONS are passed to the redis client as **kwargs

})


# 可使用多个缓存
cache2.init_app(app)
# cache2.init_app(app, config={ 'CACHE_TYPE' : 'redis','CACHE_REDIS_HOST':'172.20.3.29',
#                              'CACHE_REDIS_PORT':'6380',
#                               'CACHE_REDIS_DB':1,
#                               }
#                              )



@app.route('/', methods=["get"])
# 缓存使用时间timeout
# key_prefix 缓存使用的前缀
# @cache.memoize(50) 为使用类作为get,post对象时使用的
@cache1.cached(timeout=50, key_prefix="prefix_t2")
def test():
    msg = "hello cache"
    print(msg)
    return {"a": 1}


@app.route("/c", methods=["get"])
def c():
    cache1.clear()  # 清除缓存
    return "清除缓存成功"




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=9004)
