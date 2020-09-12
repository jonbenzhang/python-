from django.test import TestCase
from app01 import models
from django.shortcuts import HttpResponse
# Create your tests here.
def b(b):
    a = models.UserGroup.objects.all()
    b = models.UserGroup.objects.first()
    c = models.UserGroup.objects.all().first()
    d = models.UserGroup.objects.filter(id=1)
    e = models.UserGroup.objects.filter(id=1).all()
    e = models.UserGroup.objects.filter(id=1).first()
    f = models.UserGroup.objects.values()
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    return HttpResponse("hello")