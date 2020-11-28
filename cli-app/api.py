import requests


# noinspection PyShadowingBuiltins
class DatasetApi:

    def __init__(self, domain):
        self.base_uri = f'http://{domain}/datasets'

    def list(self):
        return requests.get(self.base_uri)

    def create(self, file):
        file = {
            'csv': open(file, 'rb')
        }
        return requests.post(f'{self.base_uri}/', files=file)

    def retrieve(self, id: int):
        return requests.get(f'{self.base_uri}/{id}/')

    def destroy(self, id: int):
        return requests.delete(f'{self.base_uri}/{id}/')

    def get_excel(self, id: int):
        return requests.get(f'{self.base_uri}/{id}/excel/')

    def get_stats(self, id: int):
        return requests.get(f'{self.base_uri}/{id}/stats/')

    def get_plot(self, id: int):
        return requests.get(f'{self.base_uri}/{id}/plot/')
