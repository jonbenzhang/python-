"""study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import HttpResponse
import app01
import app02
from app01.tests import b


def index(request, a1, a2):
    print(a1, a2)
    return HttpResponse(str(a1) + "-----" + str(a2))
def test(request):
    return HttpResponse("test")

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 两种匹配方法，全部使用位置或全部都有命名不可混用
    # 结束符$,如果没有结束符，/index/asdfas/adsfa.html1234 也会被匹配到index/(?P<a1>\w+)/(?P<a2>\w+).html$
    # re_path(r'index/(\w+)/(\w+)/', index),
    # re_path(r'index/(?P<a1>\w+)/(?P<a2>\w+)/', index),
    re_path(r'index/(?P<a1>\w+)/(?P<a2>\w+).html$', index),
    # 路由分发
    path("app01/", include("app01.urls")),
    path("app02/", include("app02.urls")),
    # 根据名称可以反向生成URL
    # 1. 在Python代码中
    # from django.urls import reverse
    # v = reverse('n1', kwargs={'a1': 1111})
    # { % url "m1" %}
    path('login/', test, name='m1'),
    path('test', b, name='m1'),
]
