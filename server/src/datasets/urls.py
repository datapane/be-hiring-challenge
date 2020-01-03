from rest_framework.routers import DefaultRouter

from datasets.views import DatasetViewSet

router = DefaultRouter()
router.register(r'datasets', DatasetViewSet)

urlpatterns = router.urls
