from django.urls import path

from datasets.views import (
    DatasetExportExcelView,
    DatasetExportPlotView,
    DatasetListCreateView,
    DatasetRetrieveDestroyView,
    DatasetRetrieveStatsView,
)


app_name = 'datasets'

urlpatterns = [
    path('', DatasetListCreateView.as_view(), name='dataset_list_create'),
    path('<int:pk>/', DatasetRetrieveDestroyView.as_view(), name='dataset_retrieve_delete'),
    path('<int:pk>/excel/', DatasetExportExcelView.as_view(), name='dataset_export_excel'),
    path('<int:pk>/plot/', DatasetExportPlotView.as_view(), name='dataset_export_plot'),
    path('<int:pk>/stats/', DatasetRetrieveStatsView.as_view(), name='dataset_retrieve_stats'),
]
