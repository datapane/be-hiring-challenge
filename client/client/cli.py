import json
import sys
import click

from client.datapane_client import DatapaneClient


@click.group()
def cli():
    pass


@cli.group()
def datasets():
    pass


@datasets.command()
@click.option(
    "--server", "-s", required=False, type=str, help="Server address",
)
def list(server):
    dp_client = DatapaneClient(server)
    list_of_clients = dp_client.list()
    click.echo(json.dumps(list_of_clients, indent=2))


@datasets.command()
@click.option("--server", "-s", required=False, type=str, help="Server address")
@click.argument("filepath", type=click.Path(exists=True))
def post(server, filepath):
    dp_client = DatapaneClient(server)
    instance_created = dp_client.create(filepath)
    click.echo(json.dumps(instance_created, indent=2))


@datasets.command()
@click.option(
    "--server", "-s", required=False, type=str, help="Server address",
)
@click.option("--id", "-i", type=int, required=True)
def delete(server, id):
    dp_client = DatapaneClient(server)
    dp_client.delete(id)
    click.echo("Deleted!")


@datasets.command()
@click.option("--server", "-s", required=False, type=str, help="Server address")
@click.option("--id", "-i", type=int, required=True)
def get(server, id):
    dp_client = DatapaneClient(server)
    instance_created = dp_client.get(id)
    click.echo(json.dumps(instance_created, indent=2))


@datasets.command()
@click.option("--server", "-s", required=False, type=str, help="Server address")
@click.option("--id", "-i", type=int, required=True)
def get_stats(server, id):
    dp_client = DatapaneClient(server)
    response = dp_client.stats(id)
    click.echo(json.dumps(response, indent=2))


@datasets.command()
@click.option("--server", "-s", required=False, type=str, help="Server address")
@click.option("--id", "-i", type=int, required=True)
@click.option("--destination", "-d", type=click.Path(), required=True)
def get_excel(server, id, destination):
    dp_client = DatapaneClient(server)
    dp_client.excel(id, destination)
    click.echo(f"Downloaded to {destination}")


@datasets.command()
@click.option("--server", "-s", required=False, type=str, help="Server address")
@click.option("--id", "-i", type=int, required=True)
@click.option("--destination", "-d", type=click.Path(), required=True)
def get_plot(server, id, destination):
    dp_client = DatapaneClient(server)
    dp_client.plot(id, destination)
    click.echo(f"Downloaded to {destination}")


@click.command()
def main(args=None):
    """Console script for client."""
    click.echo("See click documentation at https://click.palletsprojects.com/")
    cli()
    return 0


if __name__ == "__main__":
    sys.exit(cli())
