import click
import os
import requests

HOST = os.environ.get('APP_HOST', 'localhost')
PORT = os.environ.get('APP_PORT', '8000')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
EXCEL_FILE_PATH = os.environ.get("EXCEL_FILE_PATH", BASE_DIR)
PDF_FILE_PATH = os.environ.get("PDF_FILE_PATH", BASE_DIR)
BASE_URL = "http://{0}:{1}/datasets/".format(HOST, PORT)

@click.group()
def cli():
    pass

@cli.command("list-all")
def list_all():
    request_url = BASE_URL
    response = requests.get(request_url)
    if response.status_code == 200:
        click.echo(response.json())
    else:
        click.echo({"status_code": response.status_code, "message": response.reason})

@cli.command("create")
@click.option("--file", required=True, help="Absolute file path for CSV data set")
def create(file):
    request_url = BASE_URL
    files = {'file_blob': open(file, 'rb')}
    response = requests.post(url=request_url, files=files)
    if response.status_code == 201:
        click.echo(response.json())
    else:
        click.echo({"status_code": response.status_code, "message": response.reason})

@cli.command("get")
@click.option("--id", required=True, type=int, help="id of a dataset object to be fetched")
def get(id):
    request_url = BASE_URL + "{0}/".format(id)
    response = requests.get(request_url)
    if response.status_code == 200:
        click.echo(response.json())
    else:
        click.echo({"status_code": response.status_code, "message": response.reason})

@cli.command("delete")
@click.option("--id", required=True, type=int, help="id of a dataset object to be deleted")
def delete(id):
    request_url = BASE_URL + "{0}/".format(id)
    response = requests.delete(request_url)
    if response.status_code == 204:
        click.echo({"status_code": response.status_code, "message": "deleted successfully"})
    else:
        click.echo({"status_code": response.status_code, "message": response.reason})


@cli.command("excel")
@click.option("--id", required=True, type=int, help="id of a dataset object")
def excel(id):
    request_url = BASE_URL + "{0}/excel/".format(id)
    response = requests.get(request_url)
    if response.status_code == 200:
        file_name = "temp_file.xlsx"
        with open(BASE_DIR + "/" + file_name, "wb") as file:
            file.write(response.content)
        click.echo("File downloaded successfully")
    else:
        click.echo({"status_code": response.status_code, "message": response.reason})


@cli.command("plot")
@click.option("--id", required=True, type=int, help="id of a dataset object")
def pdf(id):
    request_url = BASE_URL + "{0}/excel/".format(id)
    response = requests.get(request_url)
    if response.status_code == 200:
        file_name = "temp_file.pdf"
        with open(BASE_DIR + "/" + file_name, "wb") as file:
            file.write(response.content)
        click.echo("File downloaded successfully")
    else:
        click.echo({"status_code": response.status_code, "message": response.reason})


@cli.command("stats")
@click.option("--id", required=True, type=int, help="id of a dataset object")
def stats(id):
    request_url = BASE_URL + "{0}/stats/".format(id)
    response = requests.get(request_url)
    if response.status_code == 200:
        click.echo(response.json())
    else:
        click.echo({"status_code": response.status_code, "message": response.reason})


if __name__ == '__main__':
    cli()
