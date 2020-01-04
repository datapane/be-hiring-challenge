import re

import click

from client import DatasetClient


api_client = DatasetClient('127.0.0.1', '8000')


@click.group()
def api():
    """A CLI wrapper for the Dataset API."""


@api.command('list')
def list_dataset():
    """List all datasets."""
    response = api_client.list()
    click.echo(response)


@api.command('create')
@click.option(
    '-f',
    '--file',
    required=True,
    prompt=False,
    type=click.Path(exists=True, readable=True),
    help='Path for CSV file'
)
def create_dataset(file):
    """Create dataset from CSV file."""
    response = api_client.create(file)
    click.echo(response)


@api.command('get')
@click.argument('dataset_id', type=int)
def retrieve_dataset(dataset_id):
    """Retrieve a single dataset."""
    response = api_client.retrieve(dataset_id)
    click.echo(response)


@api.command('stats')
@click.argument('dataset_id', type=int)
def retrieve_dataset_stats(dataset_id):
    """Retrieve a single dataset's stats."""
    response = api_client.stats(dataset_id)
    click.echo(response)


@api.command('delete')
@click.argument('dataset_id', type=int)
def delete_dataset(dataset_id):
    """Delete a single dataset."""
    response = api_client.delete(dataset_id)
    if response.status_code == 204:
        click.echo('Dataset deleted')
    else:
        click.echo(response.json())

@api.command('excel')
@click.argument('dataset_id', type=int)
def dataset_export_excel(dataset_id):
    """Export a single dataset to excel file."""
    response = api_client.excel(dataset_id)

    if response.status_code == 200:
        filename = re.findall(
            'filename="(.+)"',
            response.headers['content-disposition']
        )[0]

        with open(filename, 'wb') as f:
            f.write(response.content)

        click.echo(f'Downloaded {filename}')
    else:
        click.echo(response.json())


@api.command('plot')
@click.argument('dataset_id', type=int)
def dataset_export_plot(dataset_id):
    """Export dataset's histogram plot to PDF file."""
    response = api_client.plot(dataset_id)

    if response.status_code == 200:
        filename = re.findall(
            'filename="(.+)"',
            response.headers['content-disposition']
        )[0]

        with open(filename, 'wb') as f:
            f.write(response.content)

        click.echo(f'Downloaded {filename}')
    else:
        click.echo(response.json())
