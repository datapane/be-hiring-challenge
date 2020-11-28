from django.core.validators import FileExtensionValidator
from rest_framework import serializers

from .models import DatasetModel


class DatasetSerializer(serializers.ModelSerializer):
    """
    Serializes for List and Create methods
    """
    csv = serializers.FileField(write_only=True,
                                validators=[FileExtensionValidator(['csv'])])
    name = serializers.CharField(read_only=True)
    uri = serializers.HyperlinkedIdentityField(
        view_name='retrieve_dataset',
        lookup_field='id'
    )

    class Meta:
        model = DatasetModel
        fields = ['id', 'name', 'csv', 'uri', ]


class DatasetRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes for Retrieve method
    """
    excel = serializers.HyperlinkedIdentityField(
        view_name='retrieve_dataset_excel',
        lookup_field='id'
    )
    stats = serializers.HyperlinkedIdentityField(
        view_name='retrieve_dataset_stat',
        lookup_field='id'
    )
    plot = serializers.HyperlinkedIdentityField(
        view_name='retrieve_dataset_plot',
        lookup_field='id'
    )

    class Meta:
        model = DatasetModel
        fields = [
            'id',
            'name',
            'size',
            'stats',
            'excel',
            'plot',
        ]
