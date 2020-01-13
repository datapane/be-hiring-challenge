from rest_framework import routers

from .views import DatasetViewSet

router = routers.SimpleRouter()
router.register(r'', DatasetViewSet)

router_url_pattern = router.urls
