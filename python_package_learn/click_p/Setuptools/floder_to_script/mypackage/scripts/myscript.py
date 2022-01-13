import click
from .. import aa
@click.command()
def cli():
    """Example script."""
    a =aa.p()
    click.echo(a)