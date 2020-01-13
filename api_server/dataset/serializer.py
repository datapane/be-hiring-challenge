from rest_framework import serializers
from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dataset
        fields = ['id', 'file_blob', 'filename', 'filesize']
        read_only_fields = ['filename', 'filesize']
        extra_kwargs = {
            'file_blob': {
                'write_only': True
            }
        }
