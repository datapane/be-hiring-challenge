from io import BytesIO
import os
from django.conf import settings
from django.http import HttpResponse
from rest_framework.exceptions import ParseError
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveDestroyAPIView,
    RetrieveAPIView
)
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

import pandas as pd

from .models import Dataset
from .serializers import DatasetSerializer

class DatasetListCreateAPIView(ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = DatasetSerializer
    parser_class = (FileUploadParser,)

    def get_queryset(self):
        return Dataset.objects.all()

    def perform_create(self, serializer):
        filename = self.request.FILES['csv_data']
        df = pd.read_csv(self.request.FILES['csv_data'])
        serializer.save(filename=filename, dataframe=df)

class DatasetRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()

    def get(self, request, id, *args, **kwargs):
        dataset = Dataset.objects.get(pk=id)
        return Response({
            'filename': dataset.filename,
            'size': dataset.dataframe.size
        })

class DatasetRetrieveExcelAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()

    def get(self, request, id, *args, **kwargs):
        dataset = Dataset.objects.get(pk=id)
        bytesio = BytesIO()
        excel_filename = dataset.filename.replace('.csv', '.xlsx')
        excel_writer = pd.ExcelWriter(bytesio, engine='xlsxwriter')
        df = dataset.dataframe
        df.to_excel(excel_writer, sheet_name='sheet1')
        excel_writer.save()
        bytesio.seek(0)
        response = HttpResponse(bytesio.getvalue(), content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(excel_filename)
        return response

class DatasetRetrieveStatsAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()

    def get(self, request, id, *args, **kwargs):
        dataset = Dataset.objects.get(pk=id)
        return Response(dataset.dataframe.describe())

class DatasetRetrievePlotAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()

    def get(self, request, id, *args, **kwargs):
        dataset = Dataset.objects.get(pk=id)
        plot_path = os.path.join(settings.MEDIA_ROOT, 'plot.pdf')
        df = dataset.dataframe.select_dtypes('number')
        ax = df.plot.hist()
        fig = ax.get_figure()
        fig.savefig(plot_path)
        response = {}
        with open(plot_path, 'rb') as plot_file:
            response = HttpResponse(plot_file, content_type='application/pdf')
        os.remove(plot_path)
        return response
