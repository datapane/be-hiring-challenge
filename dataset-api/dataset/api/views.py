import tempfile
from pathlib import Path

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from matplotlib import pyplot as plt
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import DatasetModel
from .serializers import DatasetSerializer

import logging

logger = logging.getLogger(__name__)

class DatasetViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = DatasetModel.objects.all()
    serializer_class = DatasetSerializer
    parser_classes = [FormParser, MultiPartParser]

    @action(detail=True, methods=["GET"])
    def excel(self, request, pk):
        data = get_object_or_404(self.get_queryset(), pk=pk)
        filepath = Path(self.get_object().file.path)
        df = pd.read_csv(filepath)
        filepath = filepath.with_suffix(".xlsx")
        excel_filename = filepath.name
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmp_filepath = tmpdirname / Path(excel_filename)
            df.to_excel(tmp_filepath)
            with open(tmp_filepath, "rb") as ed:
                excel_data = ed.read()
        response = HttpResponse(
            excel_data,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response["Content-Disposition"] = f"attachment; filename={excel_filename}"
        return response

    @action(detail=True, methods=["GET"])
    def stats(self, request, pk):
        data = get_object_or_404(self.get_queryset(), pk=pk)
        filepath = Path(self.get_object().file.path)
        df = pd.read_csv(filepath)
        data = df.describe()
        return Response(data)

    @action(detail=True, methods=["GET"])
    def plot(self, request, pk):
        data = get_object_or_404(self.get_queryset(), pk=pk)
        filepath = Path(self.get_object().file.path)
        df = pd.read_csv(filepath)
        filepath = filepath.with_suffix(".pdf")
        pdf_filename = filepath.name
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmp_filepath = tmpdirname / Path(pdf_filename)
            df.plot.hist()
            plt.savefig(tmp_filepath)
            with open(tmp_filepath, "rb") as pdata:
                excel_data = pdata.read()
        response = HttpResponse(
            excel_data,
            content_type="application/pdf'",
        )
        response["Content-Disposition"] = f"attachment; filename={pdf_filename}"
        return response
