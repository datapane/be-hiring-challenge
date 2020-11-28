"""datapane_api_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = 'rest_api'
router = routers.DefaultRouter()

router.register('', DatasetView, basename='datasets')


urlpatterns = [
    # api
    path('', include(router.urls)),
    path('datasets/', include(router.urls)),
    path('datasets/<int:pk>',single_dataset, name= 'single_dataset'),
    path('datasets/<int:pk>/delete',delete_dataset, name= 'delete_dataset'),
    path('datasets/<int:pk>/stats',describe_dataset, name= 'stats_dataset'),
    path('datasets/<int:pk>/excel',excel_dataset, name= 'excel_dataset'),
    path('datasets/<int:pk>/plot',plot_dataset, name= 'plot_dataset'),
]
