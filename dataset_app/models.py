from django.db import models
from rest_framework import serializers 

# Create your models here.

class DatasetList(models.Model):
    file_name = models.CharField(max_length=300)
    file_path = models.CharField(max_length=300)
    file_id   =  models.AutoField(primary_key=True)
    file_size = models.CharField(max_length=100)
    deleted   = models.BooleanField(default=False)

class DatasetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetList
        fields = ['file_id','file_name', 'file_size']
