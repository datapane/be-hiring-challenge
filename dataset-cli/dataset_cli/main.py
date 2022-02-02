import os
from datetime import datetime
from pathlib import Path

import requests
import typer

from .globals import default_host
from .utils import download

app = typer.Typer()
host = os.getenv("HOST", default_host)


@app.command()
def get_all():
    resp = requests.get(default_host)
    typer.echo(resp.json())


@app.command()
def get(
    id: str = typer.Argument(..., help="The id to uniquely identify the uploaded csv")
):
    resp = requests.get(f"{host}/{id}")
    typer.echo(resp.json())


@app.command()
def get_stats(
    id: str = typer.Argument(..., help="The id to uniquely identify the uploaded csv")
):
    resp = requests.get(f"{host}/{id}/stats")
    typer.echo(resp.json())


@app.command()
def excel(
    id: str = typer.Argument(..., help="The id to uniquely identify the uploaded csv"),
    output_path: str = typer.Option(
        None,
        "-op",
        help=(
            "The path where the excel will be downloaded. Default path is data/downloads"
        ),
    ),
):
    download(id=id, output_path=output_path, ext=".xlsx", route_name="excel")


@app.command()
def pdf(
    id: str = typer.Argument(..., help="The id to uniquely identify the uploaded csv"),
    output_path: str = typer.Option(
        None,
        "-op",
        help=(
            "The path where the plot pdf will be downloaded. Default path is data/downloads"
        ),
    ),
):
    download(id=id, output_path=output_path, ext=".xlsx", route_name="excel")


@app.command()
def post(
    csv_path: str = typer.Argument(
        ...,
        help=(
            "The path along with file name and extension "
            "of the csv file to be uploaded"
        ),
    )
):
    csv_path = Path(csv_path)
    csv_name = csv_path.name
    if csv_path.exists():
        with open(csv_path, "rb") as cdata:
            csv_data = cdata
            resp = requests.post(
                default_host,
                files={"file": (csv_name, csv_data, "text/csv", {"Expires": "0"})},
            )
            if resp.status_code == requests.codes["created"]:
                typer.echo(resp.json())
            else:
                error_msg = typer.style(
                    f"Unable to upload the file.",
                    fg=typer.colors.RED,
                )
                typer.echo(error_msg)
    else:
        error_msg = typer.style(
            "The file does not exist at the specified path.",
            fg=typer.colors.RED,
        )
        typer.echo(error_msg)


@app.command()
def delete(
    id: str = typer.Argument(..., help="The id to uniquely identify the uploaded csv")
):
    delete = typer.confirm("Are you sure you want to delete it?")
    if delete:
        resp = requests.delete(f"{host}/{id}")
        if resp.status_code == requests.codes["no_content"]:
            typer.echo(f"ID: {id} deleted succesfully.")
        else:
            error_msg = typer.style(
                f"Unable to delete the id {id}.",
                fg=typer.colors.RED,
            )
            typer.echo(error_msg)
    else:
        typer.echo("Delete request aborted")


if __name__ == "__main__":
    app()
