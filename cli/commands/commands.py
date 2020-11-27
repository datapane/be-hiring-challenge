import click

from actions import *


@click.command()
@click.argument('csv', type=click.Path(exists=True), nargs=1)
@click.argument('target', envvar='DT_TARGET', type=click.Path(exists=True))
def upload(csv: str,target: str):
    print(csv)
    row = ingest_dataset(csv, target)
    click.echo(row)


@click.command()
@click.argument('target', envvar='DT_TARGET', type=click.Path(exists=True))
def all(target: str):
    dataset = get_all(target)
    for data in dataset:
        click.echo(f"id is {data['id']} filename is {data['filename']}")


@click.command()
@click.argument('id', type=int, nargs=1)
@click.argument('target', envvar='DT_TARGET', type=click.Path(exists=True))
def get(id: int, target: str):
    data = get_dataset(target, id)
    click.echo(f"filename is {data['filename']} size is {data['size']} kb")


@click.command()
@click.argument('id', type=int, nargs=1)
@click.argument('excel-path', type=click.Path(exists=False))
@click.argument('target', envvar='DT_TARGET', type=click.Path(exists=True))
def to_excel(id: int, excel_path: str, target: str):
    data = get_file(target, id)
    data.to_excel(excel_path)
    click.echo("Excel Generated")


@click.command()
@click.argument('id', type=int, nargs=1)
@click.argument('target', envvar='DT_TARGET', type=click.Path(exists=True))
def generate_stats(id: int, target: str):
    data = get_file(target, id)
    click.echo(data.describe())


@click.command()
@click.argument('id', type=int, nargs=1)
@click.argument('target', envvar='DT_TARGET', type=click.Path(exists=True))
def generate_plot(id: int, target: str):
    data = get_file(target, id)
    click.echo(id)
    generate_pdf(data)


@click.command()
@click.argument('id', type=int, nargs=1)
@click.argument('target', envvar='DT_TARGET', type=click.Path(exists=True))
def delete(id: int, target: str):
    delete_rf(target, id)


@click.group()
def cli():
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
