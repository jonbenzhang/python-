
from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import HttpResponse
from app01 import views

def index(request):
    return HttpResponse("this is app01")


urlpatterns = [
    path('index.html', index),
    # 路由分发
    path(r'^login.html$', views.Login.as_view()),

]
