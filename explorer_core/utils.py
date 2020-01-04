import pandas as pd
from os.path import join

from explorer.settings import MEDIA_ROOT
from explorer_core.models import Dataset


def get_file_path(id: int) -> str:
    file_path = join(MEDIA_ROOT, f'{id}.pkl')
    return file_path


def dataset_exists(id: int) -> Dataset:
    dataset_exist = Dataset.objects.filter(id=id).exists()
    return dataset_exist


def get_dataframe(id: int) -> pd.DataFrame:
    file_path = get_file_path(id)
    data_frame = pd.read_pickle(file_path)
    return data_frame


def get_filename(id: int) -> str:
    dataset = Dataset.objects.get(id=id)
    filename = dataset.filename
    filename_without_extention = filename.split('.')[0]
    return filename_without_extention

def get_pdf_filename(filename: str) -> str:
    file_path = join(MEDIA_ROOT, f'{filename}.pdf')
    return file_path
