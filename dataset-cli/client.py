import requests


class DatasetClient:
    """A Client to Communicate with the Dataset API"""

    def __init__(self, host, port):
        self.base_url = f'http://{host}:{port}/datasets/'

    def list(self):
        return requests.get(self.base_url).json()

    def create(self, csv_file):
        file = {'csv_file': open(csv_file, 'rb')}
        return requests.post(self.base_url, files=file).json()

    def retrieve(self, id):
        return requests.get(f'{self.base_url}{id}/').json()

    def delete(self, id):
        return requests.delete(f'{self.base_url}{id}/')

    def stats(self, id):
        return requests.get(f'{self.base_url}{id}/stats/').json()

    def excel(self, id):
        return requests.get(f'{self.base_url}{id}/excel/')

    def plot(self, id):
        return requests.get(f'{self.base_url}{id}/plot/')
