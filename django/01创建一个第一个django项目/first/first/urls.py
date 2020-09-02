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
from django.shortcuts import HttpResponse, render


def login(requset):
    """
    登陆
    :param requset:存放着用户的请求的所有数据
    :return:
    """
    # 处理字符串
    # return HttpResponse("登陆成功")
    # render寻找并处理模板,render处理模板的位置可以在settings里面配置
    return render(requset, 'login.html')


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', login)
]
