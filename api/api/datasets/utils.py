import os
import tempfile
from typing import Iterator, Dict

import pandas
from django.core.files.uploadedfile import InMemoryUploadedFile

from api.datasets.types import TransformedData


def load_csv(csv: InMemoryUploadedFile):
    csv.file.seek(0)
    return pandas.read_csv(csv.file)


def filter_by_numeric_columns(iterator: Iterator) -> Dict:
    return dict(
        filter(
            lambda elem: elem[0] if elem[1] in ["int64", "float64"] else None, iterator,
        )
    )


def transform_dataframe(
    filename: str,
    dataframe: pandas.DataFrame,
    new_extension: str,
    transform_function: str,
) -> TransformedData:
    with tempfile.TemporaryDirectory() as tmp_dirname:
        tmp_path = os.path.join(tmp_dirname, filename)
        _, ext = os.path.splitext(filename)
        tmp_path = tmp_path.replace(ext, new_extension)
        new_filename = os.path.basename(tmp_path)
        getattr(dataframe, transform_function)(tmp_path)
        data = open(tmp_path, "rb")

    return TransformedData(filename=new_filename, data=data)
