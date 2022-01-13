import click


@click.command()
@click.option('--count', default=1, help='number of greetings')  # 在命令后使用 --count 参数
@click.argument('name')  # 直接写在命令后
# python add_parameter.py zhang --count 3
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()
