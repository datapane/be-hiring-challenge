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

from django.urls import path
from .views import *
urlpatterns = [
    # api
    path('datasets/', list_datasets, name='datasets'),
    path('datasets/(?P<id>[0-9]+)$',single_dataset, name= 'single_dataset'),
    path('datasets/(?P<id>[0-9]+)/delete/',delete_dataset, name= 'delete_dataset'),
    path('datasets/(?P<id>[0-9]+)/stats/',describe_dataset, name= 'stats_dataset'),
    path('datasets/(?P<id>[0-9]+)/excel',excel_dataset, name= 'excel_dataset'),
    path('datasets/(?P<id>[0-9]+)/plot',plot_dataset, name= 'plot_dataset'),
]
