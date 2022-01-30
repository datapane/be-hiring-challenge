from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
)
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Dataset
from .serializers import DatasetSerializer


class DatasetViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = DatasetSerializer
    queryset = Dataset.objects.all()
    lookup_field = "pk"
    parser_classes = (JSONParser, MultiPartParser)

    @action(detail=True, methods=["GET"])
    def excel(self, request, pk):
        serializer = self.get_serializer(self.get_object())
        data = serializer.to_excel()
        response = HttpResponse(
            data.data,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response["Content-Disposition"] = f"attachment; filename={data.filename}"
        return response

    @action(detail=True, methods=["GET"])
    def stats(self, request, pk):
        serializer = self.get_serializer(self.get_object())
        data = serializer.get_stats()
        return Response(data)

    @action(detail=True, methods=["GET"])
    def plot(self, request, pk):
        serializer = self.get_serializer(self.get_object())
        pdf_data = serializer.get_histograms_pdf()
        response = HttpResponse(pdf_data.data, content_type="application/pdf",)
        response["Content-Disposition"] = f"attachment; filename={pdf_data.filename}"
        return response
