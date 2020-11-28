import click
import sys
import os
from db_layer import TinyDBLayer
from actions import *

target = os.getenv("DT_TARGET")
db_file = "db.json"

if target is None:
    click.echo("DT_TARGET not set")
    sys.exit()


@click.command()
@click.argument('csv', type=click.Path(exists=True), nargs=1)
def upload(csv: str):
    """Upload csv and save it to database"""
    print(csv)
    row = ingest_dataset(csv, target)
    db_layer = TinyDBLayer(target, db_file)
    row = db_layer.insert(row)
    click.echo(row)


@click.command()
def all():
    """Get all dataset objects"""
    db_layer = TinyDBLayer(target, db_file)
    dataset = db_layer.all()
    dataset = get_all(dataset)
    for data in dataset:
        click.echo(f"id is {data['id']} filename is {data['filename']}")


@click.command()
@click.argument('id', type=int, nargs=1)
def get(id: int):
    """Get single Dataset based on id"""
    db_layer = TinyDBLayer(target, db_file)
    dataset = db_layer.get(id)
    if dataset:
        data = get_dataset_info(target, dataset)
        click.echo(f"filename is {data['filename']} size is {data['size']} kb")
    else:
        click.echo(f"No data with id {id}")


@click.command()
@click.argument('id', type=int, nargs=1)
@click.argument('excel-path', type=click.Path(exists=False))
def to_excel(id: int, excel_path: str):
    """Convert Dataset to excel and save it"""
    db_layer = TinyDBLayer(target, db_file)
    dataset = db_layer.get(id)
    if dataset:
        data = get_file(target, dataset)
        data.to_excel(excel_path)
        click.echo("Excel Generated")
    else:
        click.echo(f"No data with id {id}")


@click.command()
@click.argument('id', type=int, nargs=1)
def generate_stats(id: int):
    """Generate Stat based on Dataset object"""
    db_layer = TinyDBLayer(target, db_file)
    dataset = db_layer.get(id)
    if dataset:
        data = get_file(target, dataset)
        click.echo(data.describe())
    else:
        click.echo(f"No data with id {id}")


@click.command()
@click.argument('id', type=int, nargs=1)
@click.argument('pdf-path', type=click.Path(exists=False))
def generate_plot(id: int, pdf_path: str):
    """Generate Plot based on Dataset object"""

    db_layer = TinyDBLayer(target, db_file)
    dataset = db_layer.get(id)
    if dataset:
        data = get_file(target, dataset)
        generate_pdf(data, pdf_path)
    else:
        click.echo(f"No data with id {id}")


@click.command()
@click.argument('id', type=int, nargs=1)
def delete(id: int):
    """Get single Dataset based on id"""
    db_layer = TinyDBLayer(target, db_file)
    row = db_layer.get(id)
    try:
        db_layer.delete(id)
        os.remove(os.path.join(target, row["filename"]))

    except Exception as e:
        print(e)
        click.echo("Error Removing file")


@click.group()
def cli():
    """Cli to interact and generate report with datasets"""
    pass


cli.add_command(upload)
cli.add_command(all)
cli.add_command(get)
cli.add_command(to_excel)
cli.add_command(generate_stats)
cli.add_command(generate_plot)
cli.add_command(delete)

if __name__ == '__main__':
    cli()
