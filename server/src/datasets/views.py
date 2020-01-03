from rest_framework import viewsets
from rest_framework.decorators import action

from datasets.models import Dataset
from datasets.serializers import DatasetSerializer


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    @action(methods=['get'], detail=True)
    def stats(self, request, pk=None, *args, **kwargs):
        pass

    @action(methods=['get'], detail=True)
    def excel(self, request, pk=None, *args, **kwargs):
        pass

    @action(methods=['get'], detail=True)
    def plot(self, request, pk=None, *args, **kwargs):
        pass
