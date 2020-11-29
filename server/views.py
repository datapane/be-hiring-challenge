from django.shortcuts import render
from django.views import View
import json
from .models import File
from django.http import HttpResponse
import csv
import pandas as pd
from io import StringIO, TextIOWrapper
from api_server import settings
import os

# Create your views here.

class DatasetView(View):

    def getNumberOfFilesOnMediaDir(self):
        dirName = settings.MEDIA_ROOT
        files = os.listdir(dirName)
        return str(len(files))

    def getFormattedDateTime(self, datetime): 
        date = "/".join([str(datetime.year), str(datetime.month), str(datetime.day)])
        time = ":".join([str(datetime.hour), str(datetime.minute), str(datetime.second)])
        return date + " " + time

    def post(self, request): 
        params = request.FILES["file"]
        file = params.read().decode("utf-8")
        reader = csv.DictReader(StringIO(file))
        data = [line for line in reader]
        columnNames = data[0].keys()
        dataFrame = pd.DataFrame(data, columns=columnNames)
        filePath = settings.MEDIA_ROOT + params.name
        try: 
            dataFrame.to_csv(filePath, index=False)
            fileObject = File(
                fileName = params.name,
                fileSize = params.size
            )
            fileObject.save()
            return HttpResponse(
                json.dumps(
                    {
                        "filePath": filePath,
                        "fileName" : params.name,
                        "message": "File saved as pandas dataframe successfully !",
                        "id": fileObject.id
                    }
                ),
                status=200
            )
        except Exception as e: 
            return HttpResponse(
                json.dumps(
                    str(e)
                ),
                status=500
            )

    def get(self, request): 
        allFileObjects = File.objects.all()
        formatted = [
            {
                "fileName": file.fileName,
                "fileSize": file.fileSize,
                "insertedAt": self.getFormattedDateTime(file.insertedAt),
                "updatedAt": self.getFormattedDateTime(file.updatedAt),
                "id": file.id
            }
            for file in allFileObjects
        ]
        return HttpResponse(
            json.dumps(formatted),
            status=200
        )