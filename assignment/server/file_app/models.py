from django.db import models

class File(models.Model):
	"""A class used to represent the dataset
    ...

    Attributes
    ----------
    file : FileField
        file object to store the path where the file is stored
    description : str
        the description/name of the dataset
    timestamp : DateTimeObject
        the timestamp when the file object is created
	"""
	file = models.FileField(blank=False, null=False)
	description = models.CharField(max_length=20)
	timestamp = models.DateTimeField(auto_now_add=True)