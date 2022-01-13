import fire


def hello(name):
    return 'Hello {name}!'.format(name=name)


if __name__ == '__main__':
    # 直接指定运行hello函数
    fire.Fire(hello)
# 启动命令
# zhangmeng为传递的参数
# $ python example2.py zhang
# Hello zhang!

