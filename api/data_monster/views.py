from io import BytesIO
from wsgiref.util import FileWrapper
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from actions.dataset_actions import *
from django.conf import settings
from django.http import HttpResponse, FileResponse
import os
import pandas as pd

from .serializers import FileTrackerSerializer
from .models import FileTracker


class Dataset(APIView):
    parser_classes = (MultiPartParser,)

    def get(self, request: Request):
        """Get all dataset objects"""
        all = FileTracker.objects.all()
        return Response(FileTrackerSerializer(all, many=True).data)

    def post(self, request: Request, format='csv'):
        """Upload csv and save it to database"""

        file_obj = request.FILES["dataset"]
        file_name = file_obj.name.split(".")[0]
        file_dict = ingest_dataset(file_obj.file, settings.FILE_STORAGE, file_name)
        tracker = FileTracker()
        tracker.file.name = os.path.join(settings.FILE_STORAGE, file_dict["filename"])
        tracker.save()
        return Response(FileTrackerSerializer(tracker).data)


class GetDelDataset(APIView):

    def get(self, request: Request, id: int):
        """Get single Dataset based on id"""

        try:
            tracker = FileTracker.objects.get(id=id)
        except FileTracker.DoesNotExist as e:
            return Response(status=404)

        return Response(get_dataset_info(settings.FILE_STORAGE, tracker.to_json()))

    def delete(self, request: Request, id: int):
        """Get single Dataset based on id"""

        try:
            tracker = FileTracker.objects.get(id=id)
        except FileTracker.DoesNotExist as e:
            return Response(status=404)
        os.remove(tracker.file.name)
        tracker.delete()
        return Response(status=200)


class GetStat(APIView):
    def get(self, request: Request, id: int):
        """Generate Stat based on Dataset object"""
        try:
            tracker = FileTracker.objects.get(id=id)
        except FileTracker.DoesNotExist as e:
            return Response(status=404)

        data = tracker.get_cached_result()
        if data is None:
            data = get_file(settings.FILE_STORAGE, tracker.to_json())
            tracker.set_cached_result(data)

        return Response(data)


class GetExcel(APIView):

    def get(self, request: Request, id: int):
        """Convert Dataset to excel and save it"""
        try:
            tracker = FileTracker.objects.get(id=id)
        except FileTracker.DoesNotExist as e:
            return Response(status=404)

        data = tracker.get_cached_result()
        if data is None:
            data = get_file(settings.FILE_STORAGE, tracker.to_json())
            tracker.set_cached_result(data)

        with BytesIO() as b:
            writer = pd.ExcelWriter(b, engine='xlwt')
            data.to_excel(writer)
            writer.save()
            response = HttpResponse(b.getvalue(), content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = f'attachment; filename={tracker.get_file_name()}.xls'
            return response


class GetPDF(APIView):

    def get(self, request: Request, id: int):
        """Generate Plot based on Dataset object"""

        try:
            tracker = FileTracker.objects.get(id=id)
        except FileTracker.DoesNotExist as e:
            return Response(status=404)

        file_location = os.path.join(settings.FILE_STORAGE, tracker.get_file_name() + ".pdf")
        data = tracker.get_cached_result()
        if data is None:
            data = get_file(settings.FILE_STORAGE, tracker.to_json())
            tracker.set_cached_result(data)
        generate_pdf(data, file_location)
        file_obj = FileWrapper(open(file_location, 'rb'))
        response = HttpResponse(file_obj, content_type='application/force-download')
        response['Content-Disposition'] = f'inline; filename={tracker.get_file_name()}.pdf'
        os.remove(file_location)
        return response
