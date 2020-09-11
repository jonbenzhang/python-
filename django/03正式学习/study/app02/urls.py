
from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("this is app02")


urlpatterns = [
    path('index.html', index),
    # 路由分发

]
