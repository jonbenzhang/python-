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
在配置文件中注册自己创建的app
```shell script
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
    'app02'
]
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
    # 结束符$,结束符在path中不用使用，如果没有结束符，/index/asdfas/adsfa.html1234 也会被匹配到index/(?P<a1>\w+)/(?P<a2>\w+).html$
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
##　ORM(操作数据库)
app 下的migration下存的数据库的变更记录不要轻易删除
### mysql配置使用
python3  mysql可以使用pymysql和mysqlclient,
* pymysql,使用python写的用的更方便 
* mysqlclient速度更快，因为是用c语言
* django3.1.1默认使用mysqlclient,有版本检测，因为pymysql没有那个版本所以强行修改版本号，来达到要求
在setting.py相同目录下的__init__.py写入如下代码，来配置使用pymysql
```python
import pymysql
#修改版本号django3.1.1需要 
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库
```
配置文件中添加mysql的连接
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'study_django',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': 3306,
        }
}
```
### 创建数据库
```shell script
python3 manage.py migrate   # 第一次创建表结构
python3 manage.py makemigrations app01  # 当修改表结构时运行，让Django知道我们在我们的模型有一些变更,如果加app01就只修改app01
python3 manage.py migrate app01   # 创建表结构,如果加app01就只创建app01
```
### 单表增删改差
```
# 增加
models.UserGroup.objects.create(title='销售部')
# 删除
models.UserGroup.objects.filter(id=2).delete()
# 修改
models.UserGroup.objects.filter(id=2).update(title='公关部')
# 查看
group_list = models.UserGroup.objects.all()
# filter不用加.all(),直接返回所有,可以使用first()获取第一个
group_list = models.UserGroup.objects.filter(id=1)
# id__gt=1，为大于1,__gt为大于
# id__lt=1，为小于1,__lt为小于
group_list = models.UserGroup.objects.filter(id__gt=1)
group_list = models.UserGroup.objects.filter(id__lt=1)]]
django在进行查询,会在sql语句上使用限制获取的数据条数,而不是等到拿到列表后在进行切片
所以不要在获取到数据后，再自己进行切片
models.UserInfo.objects.all()[10:20]
```
### 获取得到的表中的数据可以有三种结构
#### 1  对象/对象列表
```
# 对象列表
models.UserInfo.objects.all()
# 对象列表
models.UserInfo.objects.filter(id__gt=1)
# 对象
result = models.UserInfo.objects.first()
# 对象
models.UserInfo.objects.filter(id__gt=1).first()
```
#### 2. 字典
* 里面使用字段名
* 可进行跨表查询,ut是外键，title是外键对应表中的字典.使用ut__title查询
```
models.UserInfo.objects.values('id','name',"ut__title")
```
返回的结果
[{"id":1,"name":"fd1","ut__title":"tt1"},{"id":2,"name":"fd2","ut__title":"tt2"}]
#### 3. 元组
* 里面使用字段名
* 可进行跨表查询,ut是外键，title是外键对应表中的字典.使用ut__title查询
```
models.UserInfo.objects.values_list('id','name',"ut__title)
```
返会的结果
[(1,"df1",""title1"),(2,"df2","title2")]
### 表关联
#### 正向操作
* 可进行跨表查询,ut是外键，title是外键对应表中的字典
* 使用ut查询外键关联表中的数据
```
obj = models.UserInfo.objects.first()
obj.ut.title
```
#### 反向操作
* 找到使用外键关联obj的，userinfo表所有的数据
* 就是使用要查询的表名加__set
* userinfo_set查询到的结果可使用all(),filter(),fist()这些查询使用方法
```
obj = models.UserType.objects.first()
obj.userinfo_set.all()
```
## CBV(class base views)和FBV(function base views)
使用CBV时要在后面加上 .as_view()
```
path('login.html', views.Login.as_view()),
```
定义CBV的类
```python
from django.shortcuts import render,HttpResponse
from django.views import View
class Login(View):
    """
    get     查
    post    创建
    put     更新
    delete  删除
    """
    def dispatch(self, request, *args, **kwargs):
        # 使用dispath来筛选的使用哪个函数
        # 一般使用默认的View.dispatch()
        #如有需要，可覆盖重写 
        obj = super(Login,self).dispatch(request, *args, **kwargs)
        return obj

    def get(self,request):
        return HttpResponse('Login.get')

    def post(self,request):
        print(request.POST.get('user'))
        return HttpResponse('Login.post')
```
## 分页
###自己进行分页
django在进行查询,会在sql语句上使用限制获取的数据条数,而不是等到拿到列表后在进行切片
所以不要在获取到数据后，再自己进行切片
```
models.UserInfo.objects.all()[10:20]
```
### django 中自带的分页函数
```python
from django.shortcuts import render, HttpResponse
from app01 import models
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage


def index(request):
    """
    分页
    :param request:
    :return:
    """
    # for i in range(300):
    #     name = "root" + str(i)
    #     models.UserInfo.objects.create(name=name,age=18,ut_id=1)

    current_page = request.GET.get('page')
    # 10 为每一页拥有的数据的条数
    user_list = models.UserInfo.objects.all()
    paginator = Paginator(user_list, 10)
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
    except EmptyPage as e:
        posts = paginator.page(1)
    # has_next              是否有下一页
    # next_page_number      下一页页码
    # has_previous          是否有上一页
    # previous_page_number  上一页页码
    # object_list           分页之后的数据列表
    # number                当前页
    # paginator             paginator对象,就是包含页数
    return render(request, 'index.html', {'posts': posts})

```
## django 调试工具
### django 自带的工具
可输入使用ipython执行，django项目中的函数
```shell script
python manage.py shell
```
如
```shell script
In [1]: from app01 import models                                                                                                                                                        

In [2]: models.UserGroup.objects.all()[1:2]                                                                                                                                             
Out[2]: <QuerySet [<UserGroup: UserGroup object (2)>]>
```
### django_extensions
可以显示执行的sql语句
1. 首先下载
```shell script
pip install django_extensions
```
2. 然后进行注册
在setting.py中的INSTALLED_APPS,添加django_extensions
```shell script
INSTALLED_APPS = [
    'app01',
    'app02',
    'django_extensions'
```
3. 调用
使用如下语句调用
```shell script
python manage.py shell_plus --print-sql
```