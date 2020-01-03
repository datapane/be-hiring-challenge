from django.urls import path

from explorer_core.views import DatasetList, DatasetDetails, DatasetDescribe

urlpatterns = [
    path('datasets/', DatasetList.as_view()),
    path('datasets/<int:id>/', DatasetDetails.as_view()),
    path('datasets/<int:id>/stats/', DatasetDescribe.as_view()),

]
