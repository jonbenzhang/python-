import fire


def hello(name):
    return 'Hello {name}!'.format(name=name)


if __name__ == '__main__':
    fire.Fire()

# 启动命令
# hello 为运行的函数名,zhangmeng为传递的参数
# python example.py hello zhangmeng
