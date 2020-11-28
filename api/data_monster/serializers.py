from rest_framework import serializers


class FileTrackerSerializer(serializers.Serializer):
    file = serializers.FileField()
    id = serializers.IntegerField()

    class Meta:
        fields = "__all__"

    def to_representation(self, instance):
        file_name = instance.get_file_name()
        return {"id":instance.id,"filename": file_name}