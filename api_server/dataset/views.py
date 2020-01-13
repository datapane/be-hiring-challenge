import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from io import BytesIO
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Dataset
from .serializer import DatasetSerializer
import pandas as pd
import numpy as np
import os



class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    @action(methods=['get'], detail=True)
    def stats(self, request, pk=None):
        query_obj = get_object_or_404(Dataset, pk=pk)
        df = pd.read_csv(query_obj.filepath)
        df_desc_json = json.loads(df.describe().to_json())
        return Response(df_desc_json, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def excel(self, request, pk=None):
        query_obj = get_object_or_404(Dataset, pk=pk)
        df = pd.read_csv(query_obj.filepath)
        with BytesIO() as b:
            excel_writer = pd.ExcelWriter(b, engine='xlsxwriter')
            df.to_excel(excel_writer, sheet_name='Sheet1')
            excel_writer.save()
            response = HttpResponse(b.getvalue(), content_type='application/vnd.ms-excel', status=status.HTTP_200_OK)
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(query_obj.filename.replace(".csv", '.xlsx'))
            return response

    @action(methods=['get'], detail=True)
    def plot(self, request, pk=None):
        temp_pdf_path = os.path.join('.', 'temp.pdf')
        query_obj = get_object_or_404(Dataset, pk=pk)
        df = pd.read_csv(query_obj.filepath)
        numeric_df = df.select_dtypes(include=np.number)
        hist_plot = numeric_df.plot.hist()
        figure = hist_plot.get_figure()
        figure.savefig(temp_pdf_path)
        with open(temp_pdf_path, 'rb') as pdf_content:
            response = HttpResponse(pdf_content, content_type='application/pdf')
        os.remove(temp_pdf_path)
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(query_obj.filename.replace(".csv", '.pdf'))
        return response
