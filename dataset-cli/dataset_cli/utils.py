import os
from datetime import datetime
from pathlib import Path

import requests
import typer

from .globals import default_host, download_path

host = os.getenv("HOST", default_host)


def download(id: str, output_path: str, ext: str, route_name: str):

    if not output_path:
        basename = "output"
        suffix = datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([basename, suffix])
        op = download_path / Path(filename).with_suffix(ext)
    else:
        op = Path(output_path)
    file_ext = op.suffix
    if file_ext != ext:
        error_msg = typer.style(
            f"The filename should be with {ext} extension",
            fg=typer.colors.RED,
        )
        typer.echo(error_msg)
    else:
        breakpoint()
        resp = requests.get(f"{host}/{id}/{route_name}")
        if resp.status_code == requests.codes["ok"]:
            with open(op, "wb") as fb:
                fb.write(resp.content)
            typer.echo(f"file saved at {op}")
        else:
            error_msg = typer.style(
                f"Unable to download the file.",
                fg=typer.colors.RED,
            )
            typer.echo(error_msg)
