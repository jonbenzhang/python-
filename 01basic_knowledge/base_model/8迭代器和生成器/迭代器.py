from collections.abc import Iterator  # 迭代器
from collections.abc import Iterable  # 可迭代对象

s = 'hello'

print(isinstance(s, Iterator))  # 判断是不是迭代器
print(isinstance(s, Iterable))  # 判断是不是可迭代对象

print(isinstance(iter(s), Iterator))  # 把可迭代对象转换为迭代器 iter(s)
