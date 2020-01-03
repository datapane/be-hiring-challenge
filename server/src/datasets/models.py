from django.db import models


class Dataset(models.Model):
    blob = models.FileField(upload_to='datasets', help_text='CSV file blob')
    uploaded_at = models.DateTimeField(auto_now_add=True)
