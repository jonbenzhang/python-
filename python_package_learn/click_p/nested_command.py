import click
@click.group()
def cli():
    pass

@cli.command(help='number of greetings')
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')

if __name__ == '__main__':
    cli()