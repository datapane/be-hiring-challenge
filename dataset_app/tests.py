from django.test import TestCase
from .views import DatasetApi
from django.http import HttpRequest
# Create your tests here.
def DatasetAppTest(TestCase):
    def test_get_dataset_list(self):
        dataset_view = DatasetApi()
        request = HttpRequest()
        self.assertTrue(dataset_view)
        