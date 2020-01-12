# pylint: disable=no-member
import pandas as pd
from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from .serializers import (
    DatasetListCreateSerializer,
    DatasetDetailSerializer
)
from .models import Dataset
from .utils import create_http_response_with_attachment, create_success_response


class DatasetMixin:
    queryset = Dataset.objects.all()
    lookup_field = 'id'


# pylint: disable=too-many-ancestors
class DatasetListCreateView(DatasetMixin, generics.ListCreateAPIView):
    serializer_class = DatasetListCreateSerializer
    parser_class = (FileUploadParser,)

    def perform_create(self, serializer):
        file_name = self.request.FILES['csv_data']
        df = pd.read_csv(self.request.FILES['csv_data'])
        serializer.save(file_name=file_name, dataframe=df)


class DatasetRetrieveDestroyView(DatasetMixin, generics.RetrieveDestroyAPIView):
    serializer_class = DatasetDetailSerializer


class DatasetRetrieveExcelView(DatasetMixin, generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        file = instance.get_excel()
        file_name = instance.file_name.replace('.csv', '.xls')
        content_type = 'application/ms-excel'
        response = create_http_response_with_attachment(file, content_type, file_name)

        return response


class DatasetRetrieveStatsView(DatasetMixin, generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        response = create_success_response(stats=instance.dataframe.describe())
        return response


class DatasetRetrievePlotView(DatasetMixin, generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        file = instance.get_histogram_pdf()
        file_name = instance.file_name.replace('.csv', '.pdf')
        content_type = 'application/pdf'
        response = create_http_response_with_attachment(file, content_type, file_name)

        return response
