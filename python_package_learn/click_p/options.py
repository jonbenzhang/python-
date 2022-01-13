import click
# 官网详细
# https://click.palletsprojects.com/en/7.x/options/

@click.command()
@click.option('-s', '--string-to-echo', 'string')
def echo(string):
    click.echo(string)


if __name__ == '__main__':
    echo()
