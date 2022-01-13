# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 下午3:07
# @Author  : dataport
# @File    : s.py
# @Software: PyCharm
from threading import Thread
#
# a = {}
# a["q"] = []
# b = a["q"]
# b.append("dd")
# print(a)

a = []
b = a.copy()
b.append("dd")
print(a)
class c(object):
    def __init__(self):
        self._c__a ="a"
    def g(self):
        print(self.__a)
        return self.__a
pp = c()
print(pp.g())


dd = {}
dd.setdefault("f", []).append("e")
dd.setdefault("f", []).append("e")
print(dd)
