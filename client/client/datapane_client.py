import os

from client.client import APIClient
from client.constants import DEFAULT_BASE_API
from client.models import Dataset


def store_file(destination, content):
    destination_path = os.path.dirname(destination)
    if os.path.exists(destination_path):
        open(destination, "wb").write(content)
    else:
        raise AssertionError(f"Destination folder does not exist {destination_path}")


class DatapaneClient:
    BASE_URL = "http://localhost:8000"

    def __init__(self, url=None):
        self.base_url = url or self.BASE_URL

    def list(self):
        _url = f"{DEFAULT_BASE_API}/datasets/"
        client = APIClient(base_url=self.base_url)
        response = client.get(_url)
        return [Dataset(**ds).dict() for ds in response.json()]

    def get(self, pk):
        _url = f"{DEFAULT_BASE_API}/datasets/{pk}/"
        client = APIClient(base_url=self.base_url)
        response = client.get(_url)
        return Dataset(**response.json()).dict()

    def create(self, filepath):
        _url = f"{DEFAULT_BASE_API}/datasets/"
        client = APIClient(base_url=self.base_url)
        response = client.post(_url, files={"dataframe": open(filepath, "rb")})
        return Dataset(**response.json()).dict()

    def delete(self, pk):
        _url = f"{DEFAULT_BASE_API}/datasets/{pk}/"
        client = APIClient(base_url=self.base_url)
        client.delete(_url)

    def stats(self, pk):
        _url = f"{DEFAULT_BASE_API}/datasets/{pk}/stats/"
        client = APIClient(base_url=self.base_url)
        response = client.get(_url)
        return response.json()

    def excel(self, pk, destination):
        _url = f"{DEFAULT_BASE_API}/datasets/{pk}/excel/"
        client = APIClient(base_url=self.base_url)
        response = client.get(_url)
        store_file(destination, response.content)

    def plot(self, pk, destination):
        _url = f"{DEFAULT_BASE_API}/datasets/{pk}/plot/"
        client = APIClient(base_url=self.base_url)
        response = client.get(_url)
        store_file(destination, response.content)
