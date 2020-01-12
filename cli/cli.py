# pylint: disable=redefined-builtin
import click
from rest_client import DatasetClient

client = DatasetClient()

@click.group()
def cli():
    pass


@cli.command('get-all')
def get_all():
    response = client.get_all()
    click.echo(response)

@cli.command('create')
@click.option('-f', '--file', required=True, help='Path for CSV file')
def create(file):
    response = client.create(file)
    click.echo(response)

@cli.command('get')
@click.argument('id', type=int)
def get(id):
    response = client.get(id)
    click.echo(response)

@cli.command('delete')
@click.argument('id', type=int)
def delete(id):
    response = client.delete(id)
    message = 'Deleted successfully' if response.status_code == 204 else response.json()
    click.echo(message)

@cli.command('get-stats')
@click.argument('id', type=int)
def get_stats(id):
    response = client.get_stats(id)
    click.echo(response)

@cli.command('get-excel')
@click.argument('id', type=int)
def get_excel(id):
    """Export a single dataset to excel file."""
    response = client.get_excel(id)

    if response.status_code == 200:
        file_name = f'workbook_{id}.xlsx'

        with open(file_name, 'wb') as f:
            f.write(response.content)

        click.echo(f'Successfully downloaded {file_name}')
    else:
        click.echo(response.json())

@cli.command('get-plot')
@click.argument('id', type=int)
def get_plot(id):
    """Export a single dataset to excel file."""
    response = client.get_plot(id)

    if response.status_code == 200:
        file_name = f'plot_{id}.pdf'

        with open(file_name, 'wb') as f:
            f.write(response.content)

        click.echo(f'Successfully downloaded {file_name}')
    else:
        click.echo(response.json())