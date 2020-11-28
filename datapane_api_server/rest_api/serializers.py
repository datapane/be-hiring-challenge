from rest_framework import serializers
from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):
    dataset = serializers.FileField()

    class Meta:
        model = Dataset
        fields = ('id','created_on', 'dataset_name', 'dataset')
