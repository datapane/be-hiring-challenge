from django.contrib import admin

# Register your models here.
from explorer_core.models import Dataset


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    fields = ('filename', 'size')
    list_display = ('id', 'filename', 'size', 'created_at')
