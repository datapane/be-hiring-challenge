from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.datasets.views import DatasetViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("datasets", DatasetViewSet)


app_name = "api"
urlpatterns = router.urls
