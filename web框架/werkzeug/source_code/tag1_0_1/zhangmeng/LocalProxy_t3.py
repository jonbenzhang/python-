# use Local object directly
from werkzeug.local import LocalStack
user_stack = LocalStack()
# 在堆栈中入栈两个键值对，键都命名为name;
user_stack.push({'name': 'Bob'})
user_stack.push({'name': 'John'})

def get_user():
    # 出栈这两个键值对（获取user对象）
    return user_stack.pop()


# 直接调用函数获取user对象
user = get_user()
# 打印name的value值
print(user['name'])
print(user['name'])
