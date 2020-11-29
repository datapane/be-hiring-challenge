from django.contrib import admin
from django.urls import path
from django.conf.urls import  url
from api_server import settings 
from server import views, functional_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("dataset/datasets/<int:datasetId>/", functional_views.getDataSetByDatasetId),
    path("dataset/datasets/<int:datasetId>/excel", functional_views.exportDatasetToExcel),
    path("dataset/datasets/<int:datasetId>/stats", functional_views.getFileStats),
    path("dataset/datasets/<int:datasetId>/plot", functional_views.generateAndReturnPdf),
    path("dataset/datasets",views.DatasetView.as_view()),
    path("dataset/check_file/<int:datasetId>", functional_views.checkIfFileExists)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)