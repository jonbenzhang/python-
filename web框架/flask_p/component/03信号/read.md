## 1.安装
Flask框架中的信号基于blinker,所以需要提前安装
```shell script
pip install blinker
```
## 2. flask中内置信号
```
request_started = _signals.signal('request-started')                # 请求到来前执行
request_finished = _signals.signal('request-finished')              # 请求结束后执行
  
before_render_template = _signals.signal('before-render-template')  # 模板渲染前执行
template_rendered = _signals.signal('template-rendered')            # 模板渲染后执行
  
got_request_exception = _signals.signal('got-request-exception')    # 请求执行出现异常时执行
  
request_tearing_down = _signals.signal('request-tearing-down')      # 请求执行完毕后自动执行（无论成功与否）
appcontext_tearing_down = _signals.signal('appcontext-tearing-down')# 请求上下文执行完毕后自动执行（无论成功与否）
  
appcontext_pushed = _signals.signal('appcontext-pushed')            # 请求上下文push时执行
appcontext_popped = _signals.signal('appcontext-popped')            # 请求上下文pop时执行
message_flashed = _signals.signal('message-flashed')                # 调用flask在其中添加数据时，自动触发
```


## 3.信号中注册函数
```python
def f(*args,**kwargs):
    # 自定义的信号触发函数
    print(args,kwargs)
from flask import signals
# flask内置信号函数绑定 
signals.request_started.connect(f)
```


## 4.自定义信号,注册，触发
```python
from flask.signals import _signals
xxx = _signals.signal("xxx") 
def f(*args,**kwargs):
    # 自定义的信号触发函数
    print(args,kwargs)
# 信号函数注册 
xxx.connect(f)
# 信号触发 
xxx.send("你好")
```

## 5.为了防止不同人开发时信号名字冲突
可以使用自定义的命名空间,
flask.signals._signals 为flask调用blinker.Namespace创建的命名空间
````python
from blinker import Namespace
my_signal = Namespace()
visit_signal = my_signal.signal('my_signal')
````