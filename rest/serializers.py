from rest_framework import serializers

from rest.models import DatasetModel


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetModel
        fields = ['file']
