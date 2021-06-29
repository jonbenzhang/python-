# from tag1_0_1.werkzeug.local import LocalProxy
#
# def p():
#     print("调用p")
#     return print
# p1 = LocalProxy(p)
# p1()
class b:
    # def __init__(self):
    #
        # self.xxx = "dd"
    def __get__(self, instance, owner):
        print("get")
        return self
    # def __getattribute__(self, item):
    #     return "getattribute"
    #
    # def __getattr__(self, item):
    #     return "getattr"


a = b()
print(getattr(a, "xxx"))
class c:
    def __set__(self, instance, value):
        pass
    def __set_name__(self, owner, name):
        pass
    def __setitem__(self, key, value):
        pass
    def __setattr__(self, key, value):
        pass
    def __setslice__(self, i, j, sequence):
        pass
    def __setstate__(self, state):
        pass
class d:
    def __get__(self, instance, owner):
        pass
    def __getattribute__(self, item):
        pass
    def __getattr__(self, item):
        pass
    def __getitem__(self, item):
        pass
    def __getinitargs__(self):
        pass
    def __getnewargs__(self):
        pass
    def __getstate__(self):
        pass
    def __class_getitem__(cls, item):
        pass