import os
from io import TextIOWrapper
import pandas
from tinydb import TinyDB, Query
import numpy as np
import matplotlib.backends.backend_pdf
from tinydb.operations import delete

db_file = "db.json"


def ingest_dataset(csv: TextIOWrapper, save_folder: str):
    db = TinyDB(os.path.join(save_folder, db_file))
    dataset = pandas.read_csv(csv)
    print(dataset)
    file_name = os.path.split(csv)[-1].split(".")[0]
    dataset.to_feather(os.path.join(save_folder, file_name))
    row = {"filename": file_name}
    id = db.insert(row)
    return {"id": id, **row}


def get_all(save_folder: str):
    db = TinyDB(os.path.join(save_folder, db_file))
    return [{"id": row.doc_id, "filename": row["filename"]} for row in db.all()]


def get_dataset(save_folder: str, id: int):
    db = TinyDB(os.path.join(save_folder, db_file))
    dataset = Query()
    data = db.get(doc_id = id)
    if data:
        file = data['filename']
        file_size = os.stat(os.path.join(save_folder, file)).st_size >> 10
        data = {"filename": file, "size": file_size}
    return data


def get_file(save_folder: str, id: int):
    db = TinyDB(os.path.join(save_folder, db_file))
    data = db.get(doc_id=id)
    if data:
        file = data['filename']
        target_path = os.path.join(save_folder, file)
        data = pandas.read_feather(target_path)
    return data


def delete_rf(save_folder: str, id: int):
    db = TinyDB(os.path.join(save_folder, db_file))
    dataset = Query()
    data = db.get(doc_id = id)
    if data:
        # os.remove(os.path.join(save_folder, data["filename"]))
        db.remove(doc_id = id)


def generate_pdf(dataset: pandas.DataFrame):
    pdf = matplotlib.backends.backend_pdf.PdfPages("output.pdf")
    num_pd = dataset.select_dtypes(include=[np.float, np.int])
    for col in num_pd:
        print(num_pd[col])
        num_pd[col].hist()
        pdf.savefig()

    pdf.close()
