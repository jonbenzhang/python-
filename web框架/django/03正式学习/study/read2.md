## 模板
### 母版页面继承
* 首先写好一个模板框架(母版)，剩余部分需要使用者来填充,母版中写入{% block 名称 %}{% endblock %}，在名称位置写入这部分的名称
* 然后在要使用该母版的，html页面中写入继承语句
1. 母版
```html
    {% block css %}{% endblock %}
    {% block js %}{% endblock %}
    {% block html1 %}{% endblock %}
    {% block html2 %}{% endblock %}
```
2. 继承
继承写入自己的代码:{% block 名称 %}自己的代码{% endblock %}
要继承的母版的html页文件名称为layout.html

```html
{% extends "layout.html" %}
{% block js %}
继承后自己要实现功能的代码
{% endblock %}
{% block html %}
继承后自己要实现的代码
{% endblock %}
{%  block css %}
继承后自己要实现的代码
{% endblock %}
3．示例　
母版
```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/plugin/bootstrap-3.3.7-dist/css/bootstrap.css">
    <link rel="stylesheet" href="/static/plugin/bootstrap-3.3.7-dist/fonts/">
    <link rel="stylesheet" href="/static/css/commons.css">
    {% block css %}{% endblock %}

</head>
<body>
<div class="pg-header">
    <div class="logo left">管理系统</div>
    <div class="avatar right">
        <img src="/static/images/a.jpg" alt="">
        <div class="user-info">
            <a>个人资料</a>
            <a>注销</a>
        </div>
    </div>
    <div class="rmenus right">
        <a><i class="fa fa-commenting-o" aria-hidden="true"></i>邮件</a>
        <a><i class="fa fa-envelope-o" aria-hidden="true"></i>消息</a>
    </div>
</div>
<div class="pa-body">
    <div class="menus">
        <a> <i class="fa fa-futbol-o" aria-hidden="true"></i> 班级管理</a>
            <a>学生管理</a>
            <a>老师管理</a>
    </div>
    <div class="content">
        <ol class="breadcrumb">
              <li><a href="#">首页</a></li>
              <li><a href="#">班级管理</a></li>
              <li class="active">添加班级</li>
            </ol>
        {% block html  %}{% endblock %}

    </div>
    {% block js %}{% endblock %}
</div>
</body>
</html>
```
继承
```html
{% extends "layout.html" %}
    <link rel="stylesheet" href="/static/plugin/bootstrap-3.3.7-dist/css/bootstrap.css"/>

{%  block css %}
        <style>
        .hide {
            display: none;
        }

        .shadow {
            position: fixed;
            left: 0;
            top: 0;
            right: 0;
            bottom: 0;
            background-color: black;
            opacity: 0.4;
            z-index: 999;
        }

        .modal {
            z-index: 1000;
            position: fixed;
            left: 50%;
            top: 50%;
            height: 300px;
            width: 400px;
            background-color: white;
            margin-left: -200px;
            margin-top: -150px;
        }
    </style>
{% endblock %}
{% block html %}
<h1>班级列表</h1>
<div>
    <a href="/add_class/">添加</a>
    <a onclick="showModal();">对话框添加</a>
</div>
<table class="table">
    <thead>
    <tr>
        <th>ID</th>
        <th>班级名称</th>
        <th>操作</th>
    </tr>
    </thead>
    <tbody>
    {% for row in class_list %}
        <tr>
            <td>{{ row.id }}</td>
            <td>{{ row.title }}</td>
            <td>
                <a href="/edit_class/?nid={{ row.id }}">编辑</a>
                |
                <a onclick="editModal(this)">对话框编辑</a>
                |
                <a href="/del_class/?nid={{ row.id }}">删除</a>
            </td>
        </tr>
    {% endfor %}
    </tbody>
</table>
{#    对话框和遮罩#}
<div id="shadow" class="shadow hide"></div>
<div id="modal" class="modal hide">

    <p>
        <input id="title" type="text" name="title"/>
    </p>
    <input type="button" value="提交" onclick="AjaxSend();"/><span id="errormsg"></span>
    <input type="button" value="取消" onclick="cancleModal();"/>

</div>
<div id="edit_modal" class="modal hide">
    <div>对话框编辑</div>
    {#        使用对话框进行添加#}
    <p>
        {# hidden隐藏　为了方便进行数据的处理           #}
        <input id="edit_id" type="hidden" name="id"/>
        <input id="edit_title" type="text" name="title"/>
    </p>
    <input type="button" value="提交" onclick="AjaxEditSend();"/><span id="edit_errormsg"></span>
    <input type="button" value="取消" onclick="cancleEditModal();"/>

</div>
{% endblock %}
{% block js %}
<script src="/static/plugin/jquery-1.12.4.js"></script>
<script>
    function showModal() {
        document.getElementById('shadow').classList.remove('hide');
        document.getElementById('modal').classList.remove('hide');
    }

    function editModal(_this) {
        document.getElementById('shadow').classList.remove('hide');
        document.getElementById('edit_modal').classList.remove('hide');
        /*
            1._this获取到当前的标签
            2.找到标签的父标签的两个兄弟标签
            3．把标签中的内容复制到对话框中
        */
        var row = $(_this).parent().prevAll();
        console.log(row)
        var title = $(row[0]).text();
        var id = $(row[1]).text();
        $('#edit_id').val(id)
        $('#edit_title').val(title);
    }

    function cancleModal() {
        document.getElementById('shadow').classList.add('hide');
        document.getElementById('modal').classList.add('hide');
    }

    function cancleEditModal() {
        document.getElementById('shadow').classList.add('hide');
        document.getElementById('edit_modal').classList.add('hide');
    }

    function AjaxSend() {
        $.ajax({
            url: '/modal_add_class/',
            type: 'POST',
            data: {'title': $('#title').val()},
            success: function (data) {
                // 当服务端处理完成后，返回数据时，该函数自动调用
                // data=服务端返回的值
                console.log(data);
                if (data == "ok") {
                    location.href = "/classes/";
                } else {
                    $('#errormsg').text(data);
                }
            }
        })
    }

    function AjaxEditSend() {
        $.ajax({
            url: '/modal_edit_class/',
            type: 'POST',
            data: {
                'title': $('#edit_title').val(),
                'id': $('#edit_id').val()
            },
            success: function (data) {
                // 当服务端处理完成后，返回数据时，该函数自动调用
                // data=服务端返回的值
                //　进行字符串转json
                // JSON.parse(字符串) => 对象
                // JSON.stringify(对象) => 字符串
                data = JSON.parse(data)
                console.log(data)
                if (data.code == 200) {
                    location.reload()
                } else {
                    $('#edit_errormsg').text(data.message);
                }
            }
        })
    }
</script>
{% endblock %}
```
### 倒入组件（include）
倒入xxx.html中的代码为组件
```
{% include 'xxx.html' %}
```
#### 组件代码
```pub.html
    <div>
        <h3>特别漂亮的组件</h3>
        <div class="title">标题：{{ name }}</div>
        <div class="content">内容：{{ name }}</div>
    </div>
```
倒入组件的代码
```
test.html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>

        {% include 'pub.html' %}
        {% include 'pub.html' %}  
        {% include 'pub.html' %}
    </body> 
        </html>
```
## cookie和session
### 1. Cookie是什么？
    * 保存在客户端浏览器上的键值对
### 2. Session是什么？
    * 保存在服务端的数据（本质是键值对）
    * session基于cookie实现的
    * 在cookie中存入一段字符串，通过这个字符串可以在服务器查询其对应的具体数据
### 3. session配置
```
Django默认支持Session，并且默认是将Session数据存储在数据库中，即：django_session 表中。
 
a. 配置 settings.py
 
    SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
     
    SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
    SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
    SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
    SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
    SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
    SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
    SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
 
 
 
b. 使用
 
    def index(request):
        # 获取、设置、删除Session中数据
        request.session['k1']
        request.session.get('k1',None)
        request.session['k1'] = 123
        request.session.setdefault('k1',123) # 存在则不设置
        del request.session['k1']
 
        # 所有 键、值、键值对
        request.session.keys()
        request.session.values()
        request.session.items()
        request.session.iterkeys()
        request.session.itervalues()
        request.session.iteritems()
 
 
        # 用户session的随机字符串
        request.session.session_key
 
        # 将所有Session失效日期小于当前日期的数据删除
        request.session.clear_expired()
 
        # 检查 用户session的随机字符串 在数据库中是否
        request.session.exists("session_key")
 
        # 删除当前用户的所有Session数据
        request.session.delete("session_key")
 
        request.session.set_expiry(value)
            * 如果value是个整数，session会在些秒数后失效。
            * 如果value是个datatime或timedelta，session就会在这个时间后失效。
            * 如果value是0,用户关闭浏览器session就会失效。
            * 如果value是None,session会依赖全局session失效策略。
```
### 4. cookie 使用
#### 设置cookie
```
return_data = redirect("/classes/")
import datetime
from datetime import timedelta
ct = datetime.datetime.utcnow()
v = timedelta(seconds=10)
value = ct + v
# cookie_key cookie的key值
# cookie_value cookie的value值
# expires设置cookie的超时时间
# max_age　也是设置cookie的超时时间单位秒
# salt 对cookie进行加密,默认只是后面添加了时间戳，可以通过配置进行自定义加密方式
return_data.set_signed_cookie("cookie_key", "cookie_value", expires=value, salt="qazwsx")
# 无加密,多个cookie可使用多个set_cookie
return_data.set_cookie(key,value)
```
#### cookie获取
```
# 获取未加密cookie
request.COOKIES['key']
# 获取加密cookie
request.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)
```
## 中间件
中间件的执行顺序和注册顺序相关
### 1. 中间件使用
 - 类
process_request(self,request)
process_view(self, request, view_func, view_args, view_kwargs)
process_exception(self, request, exception)
process_response(self, request, response)
process_template_view
        
### 2.注册中间件
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
## MVC,MTV
    
* models(数据库，模型)   views（html模板）    controllers（业务逻辑处理）    --> MVC
* models(数据库，模型)   templates(html模板)  views（业务逻辑处理）          --> MTV
* Django -> MTV
