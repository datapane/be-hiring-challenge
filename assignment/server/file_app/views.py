import os, csv
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import File
from .serializers import FileSerializer
import pandas as pd 
import matplotlib.pyplot as plt
from openpyxl import Workbook

class FileView(APIView):
	"""A class to handle /datasets/ endpoint
	"""

	parser_classes = (MultiPartParser, FormParser)

	def get(self, request, *args, **kwargs):
		"""Function to handle the GET request to /datasets/ endpoint
		
		Return value: Response object containing list of json objects 
					describing the uploaded datasets
		"""
	
		try:
			queryset = File.objects.all()
			response = []
			
			for files in queryset:
				data = {}
				data['id'] = files.id
				data['description'] = files.description
				response.append(data)
			file_serializer = FileSerializer
			print(response)
			return Response(response)

		except Exception as e:
			print("Error: " + str(e))
			return Response("Error: " + str(e))

	def post(self, request, *args, **kwargs):
		"""Function to handle the POST request to /datasets/ endpoint

		Return value: Response object of the uploaded dataset
		"""
		file_serializer = FileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDetail(APIView):
	"""A class to handle /datasets/<int> endpoint
	"""

	def get(self, request, id, *args, **kwargs,):
		"""Function to handle the GET request to /datasets/<int> endpoint

		Return value: Response object having file name and size of the dataset object
		"""
		try:
			file = File.objects.get(pk = id)
			response = {}
			response['description'] = file.description
			path = os.path.join(settings.MEDIA_ROOT, str(file.file))
			size = os.path.getsize(path)
			response['size'] = size
			return Response(response)

		except Exception as e:
			print("Error: " + str(e))
			return Response("Error: " + str(e))

	def delete(self, request, id, *args, **kwargs,):
		"""Function to handle the DELETE request to /datasets/<int> endpoint

		Return value: Response object having response message and path of the deleted file
		"""
		try:
			file = File.objects.get(pk = id)
			print(file.description)
			path = os.path.join(settings.MEDIA_ROOT, str(file.file))
			if os.path.isfile(path):
				os.remove(path)
			file.delete()

			response = {}
			response['message'] = "File deleted successfully"
			response['path'] = path
			return Response(response)

		except Exception as e:
			print("Error: " + str(e))
			return Response("Error: " + str(e))

class FileExcel(APIView):
	"""A class to handle /datasets/<id>/excel/ endpoint
	"""
	def get(self, request, id, *args, **kwargs,):
		"""Function to handle the GET request to /datasets/<id>/excel/ endpoint

		Return value: Response object having path of the created excel file
		"""
		try:
			file = File.objects.get(pk = id)
			csv_file_path = os.path.join(settings.MEDIA_ROOT, str(file.file))
			excel_file_path = os.path.join(settings.MEDIA_ROOT, str(file.file).replace(".csv", ".xlsx"))
			print(excel_file_path)
			
			workbook = Workbook()
			workbook_sheet = workbook.active
			with open(csv_file_path, 'r') as f:
			    for row in csv.reader(f):
			        workbook_sheet.append(row)
			workbook.save(excel_file_path)

			response = {}
			response["File path"] = excel_file_path
			return Response(response)

		except Exception as e:
			print("Error: " + str(e))
			return Response("Error: " + str(e))

class FileStats(APIView):
	"""A class to handle /datasets/<id>/stats/ endpoint
	"""
	def get(self, request, id, *args, **kwargs,):
		"""Function to handle the GET request to /datasets/<id>/stats/ endpoint

		Return value: Response object containing the stats of the dataset
		"""
		try:
			file = File.objects.get(pk = id)
			file_path = os.path.join(settings.MEDIA_ROOT, str(file.file))
			data = pd.read_csv(file_path)
			df_describe = data.describe()
			response = df_describe.to_json()
			return Response(response)

		except Exception as e:
			print("Error: " + str(e))
			return Response("Error: " + str(e))

class FilePlot(APIView):
	"""A class to handle /datasets/<id>/plot/ endpoint
	"""
	def get(self, request, id, *args, **kwargs,):
		"""Function to handle the GET request to /datasets/<id>/plot/ endpoint

		Return value: Response object having path of the created pdf file
		"""
		try:
			file = File.objects.get(pk = id)
			file_path = os.path.join(settings.MEDIA_ROOT, str(file.file))
			pdf_file_path = os.path.join(settings.MEDIA_ROOT, str(file.file).replace(".csv", ".pdf"))

			data = pd.read_csv(file_path)
			axes = data.hist()
			fig = axes[0][0].get_figure()
			fig.savefig(pdf_file_path)
			response = {}
			response["File path"] = pdf_file_path
			return Response(response)

		except Exception as e:
			print("Error: " + str(e))
			return Response("Error: " + str(e))
