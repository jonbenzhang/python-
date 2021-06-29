from flask import Flask

from flask_script import Manager, Command,Option

app = Flask(__name__)
manager = Manager(app)


# 方式1
@manager.command
def hello():
    print("hello")

# 方式1 加参数
@manager.option('-n', '--name', help='Your name')
def hello_1(name):
    print("hello", name)

@manager.command
def hello_2(name="zhang"):
    print("hello", name)


# 方式２
class Hello2(Command):
    def run(self):
        print("hello2")

# 方式2 加参数
class Hello2_1(Command):

    def __init__(self, default_name='Joe'):
        self.default_name=default_name

    def get_options(self):
        return [
            Option('-n', '--name', dest='name', default=self.default_name),
        ]

    def run(self, name):
        print("hello",  name)
manager.add_command("hello2", Hello2)  # ,"hello3":lambda :print("hello3")})
manager.add_command("hello2_1", Hello2_1)  # ,"hello3":lambda :print("hello3")})



if __name__ == "__main__":
    manager.run()
