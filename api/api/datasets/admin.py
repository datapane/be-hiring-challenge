from django.contrib import admin

from api.datasets.models import Dataset


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    pass
