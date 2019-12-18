from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
	"""Serializer class of the class File
	"""
	
	class Meta():
		model = File
		fields = ('file', 'description', 'timestamp')
