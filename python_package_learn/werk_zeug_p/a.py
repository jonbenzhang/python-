# 使用werkzeug的Local

from werkzeug.local import Local, LocalStack, LocalProxy


class Request(object):

    def __init__(self):
        self.url = 'baidu.com'


class User(object):

    def __init__(self):
        self.owner = 'www'


r = Request()
u = User()

# 使用Local
l = Local()
l.request = r
l.user = u
# request是LocalProxy对象
request = l('request')
print(request.url)

# 使用LocalStack
ls = LocalStack()
ls.push(r)
# request是LocalProxy对象
request = ls()
print(request.url)

# 显示使用LocalProxy
request = LocalProxy(l, 'request')
print(request.url)
user = LocalProxy(l, 'user')
print(user.owner)
