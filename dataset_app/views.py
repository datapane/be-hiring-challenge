from django.shortcuts import render
from pandas.io import json
from rest_framework.views import APIView
from  .models import DatasetList , DatasetListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser
from django.conf import settings
from django.core.files.storage import default_storage
from pathlib import Path
import pandas as pd
import numpy as np
import os
from django.utils.encoding import smart_str


class DatasetApi(APIView):
    parser_classes = (MultiPartParser,)

    #TODO pagination
    def get(self, request , format=None):
        """return the list of dataset  present in the db"""
        data_list = DatasetList.objects.all()
        print(data_list)
        if data_list :
            serialized_data = DatasetListSerializer(data_list ,many=True)
            return Response(serialized_data.data)
        return Response({})


    def post(self, request, format=None):

        if 'file' not in request.data:
            raise ParseError("Empty content")

        upload_file = request.FILES['file']
        file_name = upload_file.name
        file_path = settings.CSV_FOLDER+"/" + file_name
  
        file_pointer = default_storage.save(file_path,upload_file)
        file_name = Path(file_pointer).name
        file_size = str(default_storage.size(file_path) )

        dataset_object = DatasetList.objects.create(file_name=file_name,
                                        file_path=file_path , file_size=file_size )
        file_id  = dataset_object.file_id
        
        return Response({"file_id":file_id} ,status=status.HTTP_201_CREATED)

class DatasetIDApi(APIView):

    def get(self, request, id=None) :

        file_id = id
        try:
            data_list = DatasetList.objects.get(file_id=file_id)
        except DatasetList.DoesNotExist:
            data_list = None

        if data_list :
            serialized_data = DatasetListSerializer(data_list )
            return Response(serialized_data.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request , id=None):
        file_id = id

        try:
            data_list = DatasetList.objects.get(file_id=file_id,deleted=False)
        except DatasetList.DoesNotExist:
            data_list = None
            return Response(status=status.HTTP_204_NO_CONTENT)

        DatasetList.objects.filter(file_id=file_id,deleted=False).update(deleted=True)
        return Response(status=status.HTTP_204_NO_CONTENT)

class  DatasetExcelApi(APIView):

    def csv_to_excel(self, file_path:str):
        error = True
        xlsx_path = None
        try:
            dataframe =  pd.read_csv(file_path, engine="c", sep=",")

        except Exception  as ex:
            print(ex)
            return  error, xlsx_path

        xlsx_path = os.path.splitext(file_path)[0]+".xlsx"
        try :
            dataframe.to_excel(xlsx_path)
        except Exception as ex :
            return   error , xlsx_path

        error = False
        return error , xlsx_path



    def get (self, request, id=None) :
        file_id = id
        try:
            data_list = DatasetList.objects.get(file_id=file_id,deleted=False)
        except DatasetList.DoesNotExist:
            data_list = None
            return Response(status=status.HTTP_204_NO_CONTENT)

        is_file  = default_storage.exists(data_list.file_path)

        if not is_file :
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        convert_fail , xlsx_path = self.csv_to_excel(file_path=data_list.file_path)
        if convert_fail :
            Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        file_name = Path(xlsx_path).name
        response = Response(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        response['X-Sendfile'] = smart_str(xlsx_path)
        return response


class  DatasetStatApi(APIView):
    def get(self, request, id=None) :
    
        file_id = id

        try:
            data_list = DatasetList.objects.get(file_id=file_id,deleted=False)
        except DatasetList.DoesNotExist:
            data_list = None
            return Response(status=status.HTTP_204_NO_CONTENT)

        if data_list :
            file_path = data_list.file_path
            try :
                pandas_df = pd.read_csv(file_path ,sep='delimiter', header=None)
                resp_data = pandas_df.describe()
                return Response( resp_data)

            except Exception as ex :
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

        return Response(status=status.HTTP_404_NOT_FOUND)

class DatasetPlotApi(APIView):
    def get (self, request, id=None) :
        file_id = id
        try:
            data_list = DatasetList.objects.get(file_id=file_id,deleted=False)
        except DatasetList.DoesNotExist:
            data_list = None
            return Response(status=status.HTTP_204_NO_CONTENT)

        is_file  = default_storage.exists(data_list.file_path)

        if not is_file :
            return Response(status=status.HTTP_204_NO_CONTENT)
        try :
            pdf_path = os.path.splitext(data_list.file_path)[0]+".pdf"
            csv_df = pd.read_csv(data_list.file_path, sep='delimiter', header=None ,engine='python')
            hist_data = csv_df.select_dtypes(include=[np.number])
            hist_figure = hist_data.hist()
            hist_figure.figure.savefig(pdf_path)

        except Exception as ex :
            print(ex)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)   


        file_name = Path(pdf_path).name
        response = Response(content_type='application/force-download') 
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        response['X-Sendfile'] = smart_str(pdf_path)
        return response
