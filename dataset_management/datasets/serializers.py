from rest_framework import serializers

from datasets.models import Dataset


class DatasetCreateSerializer(serializers.Serializer):
    csv_file = serializers.FileField()


class DatasetListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='datasets:dataset_retrieve_delete',
        lookup_field='pk'
    )

    class Meta:
        model = Dataset
        fields = ['id', 'name', 'url']
        read_only_fields = ['id', 'name', 'url']


class DatasetDetailSerializer(serializers.HyperlinkedModelSerializer):
    excel_url = serializers.HyperlinkedIdentityField(
        view_name='datasets:dataset_export_excel',
        lookup_field='pk'
    )
    plot_url = serializers.HyperlinkedIdentityField(
        view_name='datasets:dataset_export_plot',
        lookup_field='pk'
    )
    stat_url = serializers.HyperlinkedIdentityField(
        view_name='datasets:dataset_retrieve_stats',
        lookup_field='pk'
    )

    class Meta:
        model = Dataset
        fields = [
            'id',
            'name',
            'created_at',
            'size',
            'excel_url',
            'plot_url',
            'stat_url'
        ]
