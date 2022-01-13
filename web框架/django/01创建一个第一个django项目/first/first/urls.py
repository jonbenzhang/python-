"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
这一页面为处理路由关系使用
"""
from django.contrib import admin
from django.urls import path
# HttpResponse 为处理返回数据使用
# render寻找并处理模板
# redirect进行网页跳转
from django.shortcuts import HttpResponse, render, redirect


def login(requset):
    """
    登陆
    :param requset:存放着用户的请求的所有数据
    :return:
    """
    if requset.method == "GET":
        # 获取当前页面使用GET
        # 处理字符串
        # return HttpResponse("登陆成功")
        # render寻找并处理模板,render处理模板的位置可以在settings里面配置
        return render(requset, 'login.html')
    else:
        # requset.POST获取到POST请求发送过来的值，为字典类型
        user_name = requset.POST.get("username")
        password = requset.POST.get("password")
        if user_name == "zhang" and password == "123":
            # 可以直接跳转到百度
            # return redirect("http://www.baidu.com")
            # 跳转到index
            return redirect("/index/")
        else:
            # 重新返回login.html页面
            # 传入静态页面上的msg值，不传入msg为空
            return render(requset, 'login.html', {"msg": "用户名密码输入错误"})


def index(request):
    data_dict = {
        "msg": "this is msg",
        "msg_list": ["张梦", "赵丽", "博雅"],
        "msg_dict": {"id": 0, "name": "赵丽", "father": "赵飞"},
        "user_dict_list": [
            {"id": 0, "name": "赵丽", "father": "赵飞"},
            {"id": 1, "name": "赵二", "father": "赵飞"},
            {"id": 2, "name": "赵四", "father": "赵飞"},
        ]
    }
    return render(request, "index.html", data_dict)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login),
    path('index/', index)
]
