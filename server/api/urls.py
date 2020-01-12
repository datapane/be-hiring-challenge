from django.urls import path

from . import views


app_name = 'datasets'

urlpatterns = [
    path('', views.DatasetListCreateView.as_view(), name='dataset_list_create'),
    path('<int:id>/', views.DatasetRetrieveDestroyView.as_view(), name='dataset_retrieve_delete'),
    path('<int:id>/excel/', views.DatasetRetrieveExcelView.as_view(), name='dataset_retrieve_excel'),
    path('<int:id>/stats/', views.DatasetRetrieveStatsView.as_view(), name='dataset_retrieve_stats'),
    path('<int:id>/plot/', views.DatasetRetrievePlotView.as_view(), name='dataset_retrieve_plot'),
]
