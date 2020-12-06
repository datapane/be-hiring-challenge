import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import *
import io
import pandas as pd
from pandas import DataFrame
from django.conf import settings
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.pyplot.switch_backend('Agg')



class DataPane_listViewClass(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = MultipleFilesUploadSerializer
    """
    List all date dataset or create or delete.
    """
    global simple_variable
    def get(self,request,format=None):
        try:
            
            if not settings.MEM_OBJECT:
                print("do stuff")
                message = "Please Insert data first and try again"
                return Response(message)
            return Response(settings.MEM_OBJECT)
        except Exception as e:
            error_msg = "Exception Raise here at Get..."
            return Response(error_msg)
    
    def post(self,request,format=None):
        data = {}
        csv_file = request.FILES['file_uploaded']
        if not csv_file.name.endswith('.csv'):
            return Response("helllo error")
        data_set = csv_file.read().decode('UTF-8')
        file_name = str(csv_file)
        io_string = io.StringIO(data_set) 
        simple_variable = pd.read_csv(io_string)
        data['id'] = settings.COUNTER
        data['file_name'] =file_name
        data['data'] = data_set
        settings.MEM_OBJECT.append(data)
        settings.COUNTER +=1
        return Response(data['id'])


class DataPane_listProcessClass(APIView):

    def get(self,request,id):
        
        try:
            if not settings.MEM_OBJECT:
            
                message = "Data Not Found"
                final_data = message
            elif settings.MEM_OBJECT:
                data_obj = settings.MEM_OBJECT
                for item in settings.MEM_OBJECT:
                    if item['id']==int(id):
                        final_data = item
                        return Response(final_data)
                    return Response(final_data)
            return Response(final_data)
        except Exception as e:
            error_msg = "Exception occur at DataPane_listProcessClass."
            return Response(error_msg)
    
    def delete(self,request,id):
        try:
            if not settings.MEM_OBJECT:
            
                message = "Data Not Found"
                final_data = message
            elif settings.MEM_OBJECT:
                data_obj = settings.MEM_OBJECT
                for item in settings.MEM_OBJECT:
                    if item['id']==int(id):
                        settings.MEM_OBJECT.remove(item)
                        final_data = settings.MEM_OBJECT
                        if not settings.MEM_OBJECT:
                            final_data = "No data left in memory"
                        return Response(final_data)
                    return Response(final_data)  
            return Response(final_data)
        except Exception as e:

            error_msg = "Exception at delete"
            return Response(error_msg)


class datapane_ExcelClass(APIView):

    def get(self,request,id):
        try:
            if not settings.MEM_OBJECT:

                message = "Data Not Found"
                final_data = message
            elif settings.MEM_OBJECT:
                for item in settings.MEM_OBJECT:
                    if item['id']==int(id):
                        data_object = item['data']
                        io_string = io.StringIO(data_object) 
                        csv_df = pd.read_csv(io_string)
                        csv_df.to_excel("ouput.xlsx")
                        final_data = "File is created..."
                    return Response(final_data)  
            return Response(final_data)
           
        except Exception as e:
            return Response(e)

class datapane_StatsClass(APIView):

    def get(self,request,id):
        
        try:
            if not settings.MEM_OBJECT:
           
                message = "Data Not Found"
                final_data = message
            elif settings.MEM_OBJECT:
                for item in settings.MEM_OBJECT:
                    if item['id']==int(id):
                        data_object = item['data']
                        io_string = io.StringIO(data_object) 
                        csv_df = pd.read_csv(io_string)
                        final_data = csv_df.describe().to_json()
                    return Response(final_data)  
            return Response(final_data)
           
        except Exception as e:
            return Response(e)

class DataPane_PlotClass(APIView):

    def get(self,request,id):
        
        try:
            if not settings.MEM_OBJECT:
            
                message = "Data Not Found"
                final_data = message
            elif settings.MEM_OBJECT:
                for item in settings.MEM_OBJECT:
                    if item['id']==int(id):
                        data_object = item['data']
                        io_string = io.StringIO(data_object) 
                        csv_df = pd.read_csv(io_string)
                        # fig = plt.figure(figsize = (8,8))
                        # ax = fig.gca()
                        # csv_df.hist(ax=ax)
                        hist_object = csv_df.select_dtypes(include=[np.number]).hist()
                        final_data=plt.savefig('/Users/surjitsingh/assign/datapane/datapane/figure.pdf')
                    return Response(final_data)  
            return Response(final_data)
            
        except Exception as e:
            return Response(e)