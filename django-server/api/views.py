from django.http import HttpResponse
from django.shortcuts import render
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

class DatasetRetrieveStatsAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()

class DatasetRetrievePlotAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()
