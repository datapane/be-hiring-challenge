from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DatasetsConfig(AppConfig):
    name = "api.datasets"
    verbose_name = _("Datasets")

    def ready(self):
        try:
            import api.datasets.signals  # noqa F401
        except ImportError:
            pass
