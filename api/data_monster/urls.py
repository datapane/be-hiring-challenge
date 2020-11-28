from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('datasets/',Dataset.as_view()),
    path('datasets/<int:id>',GetDelDataset.as_view()),
    path('datasets/<int:id>/stats', GetStat.as_view()),
    path('datasets/<int:id>/excel', GetExcel.as_view()),
    path('datasets/<int:id>/plot', GetPDF.as_view())

]