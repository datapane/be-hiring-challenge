import os
from io import TextIOWrapper
import pandas
import numpy as np
import matplotlib.backends.backend_pdf


def ingest_dataset(csv: TextIOWrapper, save_folder: str,file_name=None):
    """Convert csv to feather object and save it"""

    dataset = pandas.read_csv(csv)
    if file_name is None:
        file_name = os.path.split(csv)[-1].split(".")[0]
    dataset.to_feather(os.path.join(save_folder, file_name))
    file_dict = {"filename": file_name}
    return file_dict
    # id = db_layer.insert(row)
    # return {"id": id, **row}


def get_all(dataset:list):
    return [{"id": row.doc_id, "filename": row["filename"]} for row in dataset]


def get_dataset_info(save_folder: str, data: dict):
    """Get Dataset File Name and size of file"""
    file = data['filename']
    file_size = os.stat(os.path.join(save_folder, file)).st_size >> 10
    data = {"filename": file, "size": file_size}
    return data


def get_file(save_folder: str, data: dict):
    """Get Dataset Object data"""
    file = data['filename']
    target_path = os.path.join(save_folder, file)
    data = pandas.read_feather(target_path)
    return data


def generate_pdf(dataset: pandas.DataFrame, pdf: str):
    """Generate PDF base on Dataset Object"""
    pdf = matplotlib.backends.backend_pdf.PdfPages(pdf)
    num_pd = dataset.select_dtypes(include=[np.float, np.int])
    for col in num_pd:
        num_pd[col].hist()
        pdf.savefig()

    pdf.close()
