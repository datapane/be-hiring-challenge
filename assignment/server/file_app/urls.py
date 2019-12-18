from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
	path('', FileView.as_view(), name='file-upload'),
	path('<int:id>/', FileDetail.as_view(), name='file-detail'),
	path('<int:id>/excel/', FileExcel.as_view(), name='file-excel'),
	path('<int:id>/stats/', FileStats.as_view(), name='file-stats'),
	path('<int:id>/plot/', FilePlot.as_view(), name='file-plot'),
]