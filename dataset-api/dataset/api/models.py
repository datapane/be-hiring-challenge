from django.db import models


class DatasetModel(models.Model):
    file = models.FileField(upload_to="uploads/")
    obj_size = models.IntegerField(default=0)
