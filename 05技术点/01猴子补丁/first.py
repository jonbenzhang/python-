class Monkey:
    def hello(self):
        print('hello')

    def world(self):
        print('world')


def other_fun(a=1):
    print(a)



monkey = Monkey()
monkey.hello = monkey.world
monkey.hello()
monkey.world = other_fun
monkey.world()