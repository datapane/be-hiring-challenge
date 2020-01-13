from django.db import models

class Dataset(models.Model):
    file_blob = models.FileField(upload_to='static')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} {1}".format(self.id, self.file_blob.name)

    @property
    def filename(self):
        return self.file_blob.name.split("/")[-1]

    @property
    def filesize(self):
        return self.file_blob.size

    @property
    def filepath(self):
        return self.file_blob.path
