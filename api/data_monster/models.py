import pandas as pd

from django.db import models
from django.conf import settings
from django.core.cache import cache
from redis.exceptions import ConnectionError


# Create your models here.

class FileTracker(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=settings.FILE_STORAGE)
    uploaded_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def get_file_name(self):
        return self.file.name.split("/")[-1]

    def to_json(self):
        return {"id": self.id, "filename": self.get_file_name()}

    def set_cached_result(self, data: pd.DataFrame):
        try:
            cache.set(self.id, data.to_json())
        except ConnectionError as e:
            print("Redis Inactive")

    def get_cached_result(self):
        try:
            data = cache.get(str(self.id))
            if data:
                return pd.read_json(data)
            else:
                return None
        except ConnectionError as e:
            return None
