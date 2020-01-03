from rest_framework import serializers
from os.path import basename

from datasets.models import Dataset


class DatasetSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField('get_name')
    size = serializers.SerializerMethodField('get_size')

    class Meta:
        model = Dataset
        fields = ['id', 'name', 'size', 'blob']
        extra_kwargs = {
            'blob': {'write_only': True},
        }

    def get_size(self, obj):
        return obj.blob.size

    def get_name(self, obj):
        return basename(obj.blob.name)
