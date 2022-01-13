import click


# 官网详细
# https://click.palletsprojects.com/en/7.x/arguments/
@click.command()
@click.argument('filename')
def touch(filename):
    """Print FILENAME."""
    click.echo(filename)


if __name__ == '__main__':
    touch()
