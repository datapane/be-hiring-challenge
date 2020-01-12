from rest_framework import serializers
from .models import Dataset


class DatasetListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ('id', 'file_name', 'created_time', 'modified_time')
        read_only_fields = ('file_name', 'created_time', 'modified_time')


class DatasetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ['id', 'file_name', 'size', 'created_time', 'modified_time']
