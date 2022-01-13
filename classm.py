def f(*args, **kwargs):
    print(args, kwargs)


# object.__new__=f
class c:
    pass
    # def __new__(cls, *args, **kwargs):
    #     pass
    # return object.__new__(cls)


class b():
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, a=None):
        print("init", a)
        self.h = a
b()

# n = object.__new__(b)
# print(n.h)
