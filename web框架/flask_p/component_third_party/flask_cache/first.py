#!/usr/bin/env python
# encoding: utf-8
from flask_old import Flask
from flask_cache import Cache

app = Flask(__name__)
# Check Configuring Flask-Cache section for more details
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route('/')
@cache.cached()
def index():
    print("index called")
    return "Hello World"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
