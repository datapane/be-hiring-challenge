"""datasets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.response import Response
from rest_framework.views import APIView

# noinspection PyUnresolvedReferences,PyPackageRequirements
from rest import views


class ApiDocsView(APIView):
    @staticmethod
    def get(request):
        """
        Creates Docs for Browsable API

        :param request:
        :return: Response
        """
        api_docs = {
            'datasets': request.build_absolute_uri('datasets/'),
        }
        return Response(api_docs)


urlpatterns = [
    path('', ApiDocsView.as_view()),
    path('admin/', admin.site.urls),
    path('datasets/', views.ListCreateDatasetView.as_view()),
    path('datasets/<int:id>/', views.RetrieveDestroyDatasetView.as_view(), name='retrieve_dataset'),
    path('datasets/<int:id>/stats/', views.RetrieveDatasetStatView.as_view(), name='retrieve_dataset_stat'),
    path('datasets/<int:id>/excel/', views.RetrieveDatasetExcelView.as_view(), name='retrieve_dataset_excel'),
    path('datasets/<int:id>/plot/', views.RetrieveDatasetPlotView.as_view(), name='retrieve_dataset_plot'),
]
