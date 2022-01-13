# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 上午11:41
# @Author  : dataport
# @File    : __init__.py.py
# @Software: PyCharm
from itertools import chain
a = chain({3:4,4:5},[2,3])
# a = [1]+[2,3]
for i in a:
    print(i)