import os
from os.path import join
from typing import Optional

from django.http import JsonResponse, Http404

# Create your views here.
from rest_framework import renderers
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from explorer_core.models import Dataset
from explorer_core.serializers import DatasetSerializer
import pandas as pd

from explorer_core.utils import get_file_path


class DatasetList(APIView):
    parser_class = (FileUploadParser,)
    renderer_classes = [renderers.JSONOpenAPIRenderer]

    def get(self, request):
        all_dataset = Dataset.objects.all()
        serializer = DatasetSerializer(all_dataset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        file_content = request.data['file']
        try:
            dataset = self._create_dataset(file_content)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
        try:
            dataset_id = self._write_pickled_file(file_content, dataset)
            return JsonResponse({'id': dataset_id})
        except Exception as e:
            dataset.delete()
            return JsonResponse({'message': str(e)}, status=400)

    def _create_dataset(self, file_content: str) -> Dataset:
        dataset = Dataset()
        dataset.filename = file_content.name
        dataset.size = file_content.size
        dataset.save()
        return dataset

    def _write_pickled_file(self, file_content: str, dataset: Dataset) -> int:
        data_frame = pd.read_csv(file_content)
        file_path = get_file_path(dataset.id)
        data_frame.to_pickle(file_path)
        return dataset.id


class DatasetDetails(APIView):

    def get(self, request, id):
        try:
            dataset = Dataset.objects.get(id=id)
            response = self._create_response(dataset)
            return response
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

    def _create_response(self, dataset: Dataset) -> JsonResponse:
        resp = {'filename': dataset.filename, 'size': dataset.size}
        return JsonResponse(resp)

    def delete(self, request, id):
        try:
            dataset = Dataset.objects.get(id=id)
            dataset.delete()
            self._delete_pickle(id)
            return JsonResponse({'message': 'Deleted'})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)

    def _delete_pickle(self, id):
        file_path = get_file_path(id)
        os.remove(file_path)


class DatasetDescribe(APIView):

    def get(self, request, id):
        dataset_exists = Dataset.objects.get(id=id)
        if dataset_exists:
            file_path = get_file_path(id)
            data_frame = pd.read_pickle(file_path)
            describe_json = data_frame.describe().to_json()
            return JsonResponse(describe_json, safe=False)
        else:
            return JsonResponse({'message': "Dataset doesn't exists"}, status=400)
