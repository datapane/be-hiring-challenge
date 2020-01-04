import click

from api import DatapaneApi

datapane_api = DatapaneApi()


@click.group()
@click.version_option()
def cli():
    """Starting point for all the commands
    """


@cli.group()
def datasets():
    """
        For semantic query to datasets
    :return:
    """


@datasets.command('show')
def get_all_dataset():
    all_datasets = datapane_api.get_all_datasets()
    if all_datasets:
        click.echo(all_datasets)
    else:
        click.echo("No Datasets To Show!")

@datasets.command('create')
@click.option('--filename', required=True, help="File path to upload")
def create_dataset(filename):
    created_dataset = datapane_api.create_dataset(filename)
    click.echo(f"Dataset created with id: {created_dataset['id']}")

@datasets.command('delete')
@click.option('--id', required=True, help="Id of the dataset to be deleted")
def delete_dataset(id):
    deleted_dataset = datapane_api.delete_dataset(id)
    click.echo(deleted_dataset['message'])

@datasets.command('get')
@click.option('--id', required=True, help="Id of the dataset to get info")
def get_dataset(id):
    dataset = datapane_api.get_dataset(id)
    click.echo(dataset)

@datasets.command('stats')
@click.option('--id', required=True, help="Id of the dataset to get stats")
def stats_dataset(id):
    dataset = datapane_api.stats(id)
    print(dataset)


@datasets.command('excel')
@click.option('--id', required=True, help="Id of the dataset to get excel")
@click.option('--filename', required=True, help="File path to write the content to")
def excel_dataset(id, filename):
    datapane_api.excel(id, filename)
    click.echo('Done!')

@datasets.command('plot')
@click.option('--id', required=True, help="Id of the dataset to get excel")
@click.option('--filename', required=True, help="File path to write the content to")
def pdf_dataset(id, filename):
    datapane_api.pdf(id, filename)
    click.echo('Done!')

