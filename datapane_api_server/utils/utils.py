import pandas as pd
from datapane_api_server.rest_api.models import Dataset
from django.core.exceptions import ObjectDoesNotExist
# retrieve all uploaded datasets
def list_uploaded_datasets():
    return Dataset.objects.all()

# create new dataset with uploaded csv
def create_dataset(dataset):
    pass

# return attributes of specific dataset
def find_dataset(id):
    try:
        dataset = Dataset.objects.get(id=id)
        return dataset
    except ObjectDoesNotExist:
        return None

#delete specific dataset

def delete_dataset(id):
    pass

# export dataset to excel
def export_to_excel(id):
    pass

#return stats for dataset

def dataset_stats(id):
    pass

# return histogram in pdf for specific dataset
def generate_histogram_in_pdf(id):
    pass