from django.db import models

# Create your models here.
class File(models.Model):
    id = models.AutoField(primary_key=True)
    fileName = models.CharField(max_length=50)
    fileSize = models.CharField(max_length=30)
    insertedAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now=True)