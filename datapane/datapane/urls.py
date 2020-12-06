"""datapane URL Configuration

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
# from django.urls import path
from django.conf.urls import  url
from .views import DataPane_listViewClass,DataPane_listProcessClass,datapane_ExcelClass,datapane_StatsClass,DataPane_PlotClass


urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^datasets/$', DataPane_listViewClass.as_view(), name='datapane_list'),
    url(r'^datasets/(?P<id>\d+)/$',DataPane_listProcessClass.as_view(), name = 'datapane_processlist'),
    url(r'^datasets/(?P<id>\d+)/excel/$',datapane_ExcelClass.as_view(), name = 'datapane_excel'),
    url(r'^datasets/(?P<id>\d+)/stats/$',datapane_StatsClass.as_view(), name = 'datapane_stats'),
    url(r'^datasets/(?P<id>\d+)/plot/$',DataPane_PlotClass.as_view(), name = 'datapane_plot'),
]
