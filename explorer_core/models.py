from django.db import models


# Create your models here.

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Dataset(TimeStampModel):
    filename = models.CharField(max_length=256, unique=True)
    size = models.FloatField()

    def __str__(self):
        return f'{self.filename} {self.size} {self.created_at}'

    class Meta:
        ordering = ['id']
