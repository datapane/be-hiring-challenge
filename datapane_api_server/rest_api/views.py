from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DatasetSerializer
from .models import Dataset
from django.core.exceptions import ObjectDoesNotExist
import pandas as pd


@api_view(['GET','POST'])
def list_datasets(request):
    if request.method == 'GET':
        datasets = Dataset.objects.all()
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        dataset_name = request.DATA.get('dataset_name')
        dataset = request.FILES.get('dataset')
        data = {'dataset_name': dataset_name, 'dataset': dataset}

        serializer = DatasetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def single_dataset(request, pk):
    try:
        dataset = Dataset.objects.get(pk=pk)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':

        df = pd.read_csv(dataset.dataset)
        content = {'file_name':dataset.dataset_name,
                   'size':len(df)
                   }
        return JsonResponse(content)


@api_view(['DELETE'])
def delete_dataset(request, pk):
    try:
        dataset = Dataset.objects.get(pk=pk)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        dataset.delete()
        return HttpResponse(status=200)


@api_view(['GET'])
def describe_dataset(request, pk):
    try:
        dataset = Dataset.objects.get(pk=pk)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        df = pd.read_csv(dataset.dataset)

        return JsonResponse(df.describe())


@api_view(['GET'])
def excel_dataset(request, pk):
    try:
        dataset = Dataset.objects.get(pk=pk)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        df = pd.read_csv(dataset.dataset)

        return HttpResponse(status=200)