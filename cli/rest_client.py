# pylint: disable=redefined-builtin
import json
import requests


class RESTClient:

    HOST = '127.0.0.1'
    PORT = '8000'
    ENDPOINT = ''

    def __init__(self):
        self.base_url = f'http://{self.HOST}:{self.PORT}/{self.ENDPOINT}/'

    def get_all(self):
        response = requests.get(self.base_url).json()
        return response

    def create(self, data):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(self.base_url, data=json.dumps(data), headers=headers).json()
        return response

    def get(self, id):
        url = f'{self.base_url}{id}/'
        response = requests.get(url).json()
        return response

    def delete(self, id):
        url = f'{self.base_url}{id}/'
        response = requests.delete(url)
        return response


class DatasetClient(RESTClient):

    ENDPOINT = 'datasets'

    # pylint: disable=arguments-differ
    def create(self, csv_file):
        csv_data = open(csv_file, 'rb')
        file = {'csv_data': csv_data}
        response = requests.post(self.base_url, files=file).json()
        return response

    def get_stats(self, id):
        url = f'{self.base_url}{id}/stats/'
        response = requests.get(url).json()
        return response

    def get_excel(self, id):
        url = f'{self.base_url}{id}/excel/'
        response = requests.get(url)
        return response

    def get_plot(self, id):
        url = f'{self.base_url}{id}/plot/'
        response = requests.get(url)
        return response
