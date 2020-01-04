import os
from io import BytesIO
from os.path import join
from typing import Optional

import numpy as np
from django.http import JsonResponse, HttpResponse

# Create your views here.
from rest_framework import renderers
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from explorer_core.models import Dataset
from explorer_core.serializers import DatasetSerializer
import pandas as pd

from explorer_core.utils import get_file_path, dataset_exists, get_dataframe, get_filename, get_pdf_filename


class DatasetList(APIView):
    """
        This class helps to get details of all the datasets available
        and also to create a dataset in the database
    """
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
    """
        This class helps in getting the details of the datasets.
    """

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
        if dataset_exists(id):
            data_frame = get_dataframe(id)
            describe_json = data_frame.describe().to_json()
            return JsonResponse(describe_json, safe=False)
        else:
            return JsonResponse({'message': "Dataset doesn't exists"}, status=400)


class DatasetExcelExporter(APIView):

    def get(self, request, id):
        if dataset_exists(id):
            data_frame = get_dataframe(id)
            data = self._get_excel_data(data_frame)
            filename = get_filename(id)
            response = self._generate_excel_response(data, filename)
            return response
        else:
            return JsonResponse({'message': "Dataset doesn't exists"}, status=400)

    def _get_excel_data(self, data_frame):
        in_memory_fp = BytesIO()
        data_frame.to_excel(in_memory_fp)
        in_memory_fp.seek(0, 0)
        data = in_memory_fp.read()
        return data

    def _generate_excel_response(self, data: bytes, filename: str) -> HttpResponse:
        response = HttpResponse(data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={filename}.xlsx'
        return response


class DatasetPdfExporter(APIView):

    def get(self, request, id):
        if dataset_exists(id):
            data_frame = get_dataframe(id)
            filename = get_filename(id)
            data = self._get_pdf_data(data_frame, filename)
            response = self._generate_pdf_response(data, filename)
            return response
        else:
            return JsonResponse({'message': "Dataset doesn't exists"}, status=400)

    def _get_pdf_data(self, data_frame: pd.DataFrame, filename: str) -> bytes:
        df_numerics_only = data_frame.select_dtypes(include=np.number)
        file_path = get_pdf_filename(filename)
        self._generate_pdf(df_numerics_only, file_path)
        data = self._get_data(file_path)
        os.remove(file_path)
        return data

    def _generate_pdf(self, df_numerics_only: pd.DataFrame, file_path: str) -> None:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_pdf import PdfPages
        with PdfPages(file_path) as pdf:
            df_numerics_only.hist()
            pdf.savefig()
            plt.close()

    def _get_data(self, file_path: str) -> bytes:
        with open(file_path, 'rb') as pdf:
            data = pdf.read()
        return data

    def _generate_pdf_response(self, data: bytes, filename: str) -> HttpResponse:
        response = HttpResponse(data, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment;filename={filename}.pdf'
        return response
