import os
import pandas as pd

from django.http import HttpResponse

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .serializers import DatasetSerializer, DatasetRetrieveSerializer
from .models import DatasetModel


class DatasetMixin:
    """
    Mixin class for all views
    """
    queryset = DatasetModel.objects.all()
    lookup_field = 'id'


class RetrieveDestroyDatasetView(DatasetMixin, RetrieveDestroyAPIView):
    """
    Returns Show and Delete Views
    """
    serializer_class = DatasetRetrieveSerializer


class ListCreateDatasetView(DatasetMixin, ListCreateAPIView):
    """
    Returns Create View
    """
    parser_classes = [MultiPartParser, ]
    serializer_class = DatasetSerializer

    def perform_create(self, serializer):
        file = serializer.validated_data.get('csv')
        return DatasetModel.objects.create(
            dataframe=pd.read_csv(file),
            name=os.path.splitext(file.name)[0]
        )

    def create(self, request, *args, **kwargs):
        request_data = self.get_serializer(data=request.data)
        request_data.is_valid(raise_exception=True)
        created_object = self.perform_create(request_data)

        response = DatasetSerializer(created_object, context={'request': request})

        return Response(response.data, status.HTTP_201_CREATED)


class RetrieveDatasetExcelView(DatasetMixin, GenericAPIView):
    """
    Exports Excel
    """

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        excel = obj.get_excel()

        response = HttpResponse(
            excel, content_type='application/ms-excel'
        )
        response['Content-Disposition'] = (
            f'attachment; filename="{obj.name}.xlsx"'
        )

        return response


class RetrieveDatasetStatView(DatasetMixin, GenericAPIView):
    """
    Returns stats
    """

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'stats': self.get_object().dataframe.describe()
            }
        )


class RetrieveDatasetPlotView(DatasetMixin, GenericAPIView):
    """
    Returns plots on PDF
    """

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        pdf = obj.get_plot()

        response = HttpResponse(
            pdf, content_type='application/pdf'
        )
        response['Content-Disposition'] = (
            f'attachment; filename="{obj.name}.pdf"'
        )

        return response
