
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DatasetSerializer
from .models import Dataset
from django.core.exceptions import ObjectDoesNotExist

import pandas as pd
from django.conf import settings

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

@api_view(['GET','POST'])
def list_datasets(request):
    if request.method == 'GET':
        datasets = Dataset.objects.all()
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        dataset_name = request.DATA.get('dataset_name')
        dataset = request.FILES.get('dataset')
        data = {'dataset_name': dataset_name, 'dataset': dataset}

        serializer = DatasetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def single_dataset(request, pk):
    try:
        dataset = Dataset.objects.get(pk=pk)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':

        df = pd.read_csv(dataset.dataset)
        content = {'file_name':dataset.dataset_name,
                   'size':len(df)
                   }
        return JsonResponse(content)


@api_view(['DELETE'])
def delete_dataset(request, pk):
    try:
        dataset = Dataset.objects.get(pk=pk)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        dataset.delete()
        return HttpResponse(status=200)


@api_view(['GET'])
def describe_dataset(request, pk):
    try:
        dataset = Dataset.objects.get(pk=pk)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        df = pd.read_csv(dataset.dataset)

        return JsonResponse(df.describe())


@api_view(['GET'])
def excel_dataset(request, pk):
    try:
        dataset = Dataset.objects.get(pk=pk)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        df = pd.read_csv(dataset.dataset)
        file_name = f'{settings.BASE_DIR}/server_files/{dataset.dataset_name}.xlsx'
        df.to_excel(file_name,index=False,header=True)

        with open(file_name, "r") as excel:
            data = excel.read()

        response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        return response


@api_view(['GET'])
def plot_dataset(request, pk):
    try:
        dataset = Dataset.objects.get(pk=pk)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        df = pd.read_csv(dataset.dataset)
        numeric_column_dataset = df.select_dtypes('number')
        file_name = f'{settings.BASE_DIR}/server_files/{dataset.dataset_name}.pdf'
        with PdfPages(file_name) as pdf_file:
            numeric_column_dataset.hist(bins=30, figsize=(15, 10))
            plt.title('Dataset Histogram', fontsize=10)
            plt.grid(True)
            pdf_file.savefig()
            plt.close()

        with open(file_name, "r") as pdf:
            data = pdf.read()

        response = HttpResponse(data, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={file_name}'
        return response
