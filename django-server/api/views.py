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
    lookup_field = 'pk'
    serializer_class = DatasetSerializer
    parser_class = (FileUploadParser,)

    def get_queryset(self):
        return Dataset.objects.all()

    def perform_create(self, serializer):
        df = pd.read_csv(self.request.FILES['csv_data'])
        serializer.save(dataframe=df)

class DatasetRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()

class DatasetRetrieveExcelAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()

class DatasetRetrieveStatsAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()

    def get(self):
        pass

class DatasetRetrievePlotAPIView(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()

    def get(self):
        pass
