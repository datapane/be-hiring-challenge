import os

import pandas as pd
from rest_framework import status
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.response import Response

from django.http import HttpResponse
from django.shortcuts import render

from datasets.models import Dataset
from datasets.serializers import (
    DatasetCreateSerializer,
    DatasetDetailSerializer,
    DatasetListSerializer,
)


class DatasetBaseMixin:
    queryset = Dataset.objects.all()
    lookup_field = 'pk'


class DatasetListCreateView(DatasetBaseMixin, ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DatasetCreateSerializer
        return DatasetListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # serialize the imported dataset
        serializer = DatasetListSerializer(
            instance=obj,
            context={'request': request}
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer):
        csv = serializer.validated_data.get('csv_file')
        dataframe = pd.read_csv(csv, encoding='utf-8')

        obj = Dataset.objects.create(
            dataframe=dataframe,
            name=os.path.splitext(csv.name)[0]
        )

        return obj


class DatasetRetrieveDestroyView(DatasetBaseMixin, RetrieveDestroyAPIView):
    serializer_class = DatasetDetailSerializer


class DatasetRetrieveStatsView(DatasetBaseMixin, GenericAPIView):

    def get(self, request, *args, **kwargs):
        instance = self.get_object()

        return Response(
            data={
                'stats': instance.dataframe.describe()
            },
            status=status.HTTP_200_OK
        )


class DatasetExportExcelView(DatasetBaseMixin, GenericAPIView):

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        excel_file = instance.to_excel()

        response = HttpResponse(
            excel_file, content_type='application/ms-excel'
        )
        response['Content-Disposition'] = (
            f'attachment; filename="{instance.name}.xls"'
        )

        return response


class DatasetExportPlotView(DatasetBaseMixin, GenericAPIView):

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        excel_file = instance.to_pdf()

        response = HttpResponse(
            excel_file, content_type='application/pdf'
        )
        response['Content-Disposition'] = (
            f'attachment; filename="{instance.name}.pdf"'
        )

        return response
