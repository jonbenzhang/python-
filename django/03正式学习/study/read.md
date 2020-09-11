# django
## 创建一个django项目
first 是要创建的项目的名称
```shell script
django-admin startproject first
```
## 目录结构

![image-20200902170152905](/home/zhangmeng/.config/Typora/typora-user-images/image-20200902170152905.png)

1.  init__.py:是项目的初始化文件有了这个文件 标志当前文件夹是一个包,可以被引用

2. settings.py:项目的配置文件，所有的django的配置信息都在这里面,包括数据库的配置,静态文件的配置,还有django依赖的第三方扩展包

3. urls.py：进行url路由的配置，通过网址对应网页

4. wsgi.py：服务器和django交互的入口

5. manage.py:是项目的管理文件

## 配置文件修改

在配置文件中有详细的修改说明

1. 配置模板路径
2. 配置静态文件路径

## django创建app
```shell script
python manage.py startapp app01
```
## 路由
### 路由分发
如appo1/aa,则到app01.urls寻找aa
```
    path("app01/", include("app01.urls")),
    path("app02/", include("app02.urls")),
```
### 路由正则匹配
url正则传递参数
```
    # 两种匹配方法，全部使用位置或全部都有命名不可混用
    # 结束符$,如果没有结束符，/index/asdfas/adsfa.html1234 也会被匹配到index/(?P<a1>\w+)/(?P<a2>\w+).html$
    # re_path(r'index/(\w+)/(\w+)/', index),
    # re_path(r'index/(?P<a1>\w+)/(?P<a2>\w+)/', index),
    re_path(r'index/(?P<a1>\w+)/(?P<a2>\w+).html$', index),
```
参数获取,使用和url相对应的参数个数来进行获取
```
def index(request, a1, a2):
    print(a1, a2)
    return HttpResponse(str(a1) + "-----" + str(a2))
```
### url命名
```
    path('login/', index, name='m1'),
    # 根据名称可以反向生成URL
    from django.urls import reverse
    v = reverse('m1', kwargs={'a1': 1111})
    # 在模板中使用m1来跳转url,后面通过空格分割来传递正则url的参数
    { % url "m1" %}
    { % url "m1" "aa" 11 %}

```