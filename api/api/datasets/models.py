import pandas
from django.db import models


class Dataset(models.Model):
    dataframe = models.FileField(upload_to="uploads/%Y/%m/%d/")
    size = models.IntegerField()

    def load_dataframe(self):
        return pandas.read_feather(self.dataframe.path)
