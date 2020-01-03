from django.shortcuts import render
from rest_framework import generics

from .models import Dataset
from .serializers import DatasetSerializer

class DatasetListCreateAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()

class DatasetRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = DatasetSerializer

    def get_queryset(self):
        return Dataset.objects.all()
