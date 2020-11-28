import click
import helpers
from api import DatasetApi

api = DatasetApi('0.0.0.0:8000')


@click.group()
def cli():
    pass


@cli.command()
def ls():
    """
    List datasets.
    """
    click.echo(api.list().json())


# noinspection PyShadowingBuiltins
@cli.command()
@click.argument('id', type=int)
def get(id):
    """
    Show a dataset.
    """
    click.echo(api.retrieve(id).json())


@cli.command()
@click.option(
    '--file',
    '-f',
    required=True,
    type=click.Path(True),
    help='Path to CSV file'
)
def create(file):
    """
    Create a dataset.
    """
    click.echo(api.create(file).json())


# noinspection PyShadowingBuiltins
@cli.command()
@click.argument('id', type=int)
def delete(id):
    """
    Delete a dataset.
    """
    response = api.destroy(id)
    if response.status_code == 204:
        click.echo('Deleted')
    else:
        click.echo(response.json())


# noinspection PyShadowingBuiltins
@cli.command()
@click.argument('id', type=int)
def excel(id):
    """
    Export a dataset as Excel.
    """
    response = api.get_excel(id)
    helpers.handle_file_response(response)


# noinspection PyShadowingBuiltins
@cli.command()
@click.argument('id', type=int)
def stats(id):
    """
    Get stats for a dataset.
    """
    click.echo(api.get_stats(id).json())


# noinspection PyShadowingBuiltins
@cli.command()
@click.argument('id', type=int)
def plot(id):
    """
    Get plot for a dataset as PDF.
    """
    response = api.get_plot(id)
    helpers.handle_file_response(response)
