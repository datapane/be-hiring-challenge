from os.path import basename
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import pandas as pd
from datasets.models import Dataset
from datasets.serializers import DatasetSerializer
from datasets.utils import ExcelConverter, PlotToPDF


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    @action(methods=['get'], detail=True)
    def stats(self, request, pk=None, *args, **kwargs):
        obj = get_object_or_404(Dataset, pk=pk)
        df = pd.read_csv(obj.blob.path)
        return Response(data={'stats': df.describe()}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def excel(self, request, pk=None, *args, **kwargs):
        obj = get_object_or_404(Dataset, pk=pk)
        response = HttpResponse(content=ExcelConverter(obj.blob.path).convert(),
                                content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(
            basename(obj.blob.name).replace(".csv", ".xlsx"))
        return response

    @action(methods=['get'], detail=True)
    def plot(self, request, pk=None, *args, **kwargs):
        obj = get_object_or_404(Dataset, pk=pk)
        response = HttpResponse(content=PlotToPDF(obj.blob.path).pdf(),
                                content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(
            basename(obj.blob.name).replace(".csv", ".pdf"))
        return response
