from django.db import models

# Create your models here.
class Dataset(models.Model):
    dataset_name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dataset_name