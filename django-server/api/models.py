from django.db import models
from picklefield.fields import PickledObjectField

class Dataset(models.Model):
    title = models.CharField(max_length=60, null=True, blank=True)
    csv_data = models.FileField(upload_to='uploads/', null=True, blank=True)
    filename = models.CharField(max_length=60, null=True, blank=True)
    dataframe = PickledObjectField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
