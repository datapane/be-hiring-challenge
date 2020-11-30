from django.shortcuts import reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.viewsets import ViewSet


from .serializers import DatasetSerializer
from .models import Dataset
from django.core.exceptions import ObjectDoesNotExist

import pandas as pd
from django.conf import settings

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


class DatasetView(ViewSet):

    serializer_class = DatasetSerializer

    def retrieve(self, request, pk=None):
        queryset = Dataset.objects.all()
        dataset = get_object_or_404(queryset, pk=pk)
        df = pd.read_csv(dataset.dataset)
        content = {
            'dataset': dataset.dataset_name,
            'file_name': dataset.filename(),
            'size': len(df)
        }
        return Response(content)


    def list(self, request):
        datasets = Dataset.objects.all()
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data)

    def create(self, request):

        if 'dataset' not in request.data:
            raise ParseError("Empty content")

        dataset_name = request.data.get('dataset_name')
        dataset = request.FILES.get('dataset')
        # perform custom validation
        if str(dataset).split('.')[1] != 'csv':
            return Response('Wrong file type. Only CSV allowed',status=status.HTTP_400_BAD_REQUEST)

        data = {'dataset_name': dataset_name, 'dataset': dataset}

        serializer = DatasetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            queryset = Dataset.objects.all()
            dataset = get_object_or_404(queryset, pk=pk)
            dataset.delete()
        except Http404:
            pass
        return HttpResponseRedirect(redirect_to=reverse('rest_api:datasets'))


    @action(detail=True)
    def describe_dataset(self, request, pk):
        try:
            dataset = Dataset.objects.get(pk=pk)

        except ObjectDoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            df = pd.read_csv(dataset.dataset)

            return Response(df.describe().to_json())


    @action(detail=True)
    def excel_dataset(self, request, pk):
        try:
            dataset = Dataset.objects.get(pk=pk)

        except ObjectDoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            df = pd.read_csv(dataset.dataset)
            file_name = f'{settings.BASE_DIR}/server_files/{dataset.dataset_name}.xlsx'
            df.to_excel(file_name, index=False, header=True)

            with open(file_name, "rb") as excel:
                response = HttpResponse(excel.read(),
                                        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = f'inline; filename={file_name.split("/")[-1]}'
                return response

    @action(detail=True)
    def plot_dataset(self, request, pk):
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
                plt.grid(True)
                pdf_file.savefig()
                plt.close()

            with open(file_name, "rb") as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'inline; filename={file_name.split("/")[-1]}'
                return response
