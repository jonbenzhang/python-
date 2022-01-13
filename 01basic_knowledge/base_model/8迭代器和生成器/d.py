def b():
    a = 1
    while a < 5:
        yield a
        a +=1

c = b()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

