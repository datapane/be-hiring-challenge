from rest_framework import serializers

from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ['id', 'title', 'filename', 'csv_data', 'dataframe', 'timestamp']
        read_only_fields = ['filename', 'timestamp']
