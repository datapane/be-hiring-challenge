from django.urls import path

from . import views

urlpatterns = [
    path('', views.DatasetApi.as_view()),
    path('<int:id>/', views.DatasetIDApi.as_view()),
    path('<int:id>/excel/', views.DatasetExcelApi.as_view()),
    path('<int:id>/stats/', views.DatasetStatApi.as_view()),
    path('<int:id>/plot/', views.DatasetPlotApi.as_view()),
]