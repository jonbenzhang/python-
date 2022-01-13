from flask_ import Flask
def a(func):
    print("a")
    def c():
        print("c")
        func()
        print("c end")
    print("a--end ")
    return c
@a
def b():
    print("b")


# print(b())