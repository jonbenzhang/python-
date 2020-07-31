# 创建生成器简单方式
a = (i for i in range(1, 10))  # 将列表生成试外部的中括号改为小括号，就能将生成式转化为生成器。
b = next(a)
print("b:", b)
c = a.__next__()
print("c:", c)
next(a), a.__next__()  # 生成器的取值方式只能使用next的方法。


def num():
    a, b = 0, 1
    for i in range(10):
        yield b  # 生成关键字yield，有yield的关键字的代码块就是yield的生成器。当运行到yield时代码就会停止，并返回运行结果，当在次运行时依旧是到yield停止，并返回结果。 切记：生成器只能使用next方法。
        print(b)
        a, b = b, a + b
        yield "奶奶个腿"
        temp = yield b  # 这里并不是变量的定义，当运行到yield时就会停止，所以当运行到等号右边的时候就会停止运行，当在次使用next的时候，将会把一个None赋值给temp，因为b的值已经在上轮循环中输出。这里可以使用num().send()方法将一个新的值赋值给temp。
        print(temp)


a = num()  # 将生成器赋值给变量a。


# for n in a:  # 生成器可以使用for循环使用，并且不会出错。
#     print(n)

def send_test():
    h = "i'm h"
    yield h
    print("h", h)
    a = "test"
    b = yield a
    print("b", b)
    d = "i'm d"
    f = yield d
    print("f", f)


# c = send_test()
# print(c.__next__())
# print("**")
d = send_test()
print(d.send("first"))
print(next(d))
print(d.send("i'm send arg"))
# def a():
#     print('aaa')
#     p1 = yield '123'
#     print('bbb')
#     if (p1 == 'hello'):
#         print('p1是send传过来的')
#     p2= yield '234'
#     print(p2)
#
# r = a()
# next(r)
# r.send('hello')
classmethod.__call__()