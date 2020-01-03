from django.urls import path

from explorer_core.views import DatasetList

urlpatterns = [
    path('datasets/', DatasetList.as_view()),
]