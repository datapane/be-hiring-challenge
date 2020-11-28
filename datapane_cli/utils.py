import pandas as pd
import glob as gb
import os, shutil

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

data_store_folder = 'data_store'
output_folder = 'output'

files = gb.glob(f'{data_store_folder}/*.csv')

def upload_dataset(path):
    source = path
    destination = data_store_folder
    shutil.copy(source, destination)
    file_name = path.split('/')[-1]
    return f'File succesfully uploaded to {destination}/{file_name}'


def list_datasets():
    return files

def single_dataset(id):
    dataset = files[id]
    df = pd.read_csv(dataset)
    content = {'file_name': (dataset.split('.')[0]).split('/')[1],
               'size': len(df)
               }
    return content

def delete_dataset(id):
    dataset = (files[id]).split("/")[1]
    os.remove(f'{data_store_folder}/{dataset}')
    return f'{dataset} successfully removed'

def describe_dataset(id):
    dataset = files[id]
    df = pd.read_csv(dataset)
    return df.describe()

def export_to_excel(id):
    dataset = files[id]
    df = pd.read_csv(dataset)
    file_name = f'{output_folder}/{dataset.split("/")[1].split(".")[0]}.xlsx'
    df.to_excel(file_name, index=False, header=True)
    return f'Export to excel successful. Find you file at the location {file_name}'

def export_to_pdf(id):
    dataset = files[id]
    df = pd.read_csv(dataset)
    numeric_column_dataset = df.select_dtypes('number')
    file_name = f'{output_folder}/{dataset.split("/")[1].split(".")[0]}.pdf'
    with PdfPages(file_name) as pdf_file:
        numeric_column_dataset.hist(bins=30, figsize=(15, 10))
        plt.title('Dataset Histogram', fontsize=10)
        plt.grid(True)
        pdf_file.savefig()
        plt.close()
    return f'Export to PDF successful. Find you file at the location {file_name}'