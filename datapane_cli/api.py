import ast
import json
import sys
from typing import Any

import requests


class DatapaneApi:
    def __init__(self):
        self.api = 'http://0.0.0.0:8000'

    def get_all_datasets(self):
        url = f'{self.api}/datasets/'
        data = self._get_request(url)
        data = self._pretty_response(data)
        return data

    def create_dataset(self, filename):
        url = f'{self.api}/datasets/'
        data = self._post_request(url, filename)
        return data

    def get_dataset(self, id):
        url = f'{self.api}/datasets/{id}/'
        data = self._get_request(url)
        data = self._pretty_response(data)
        return data

    def stats(self, id):
        url = f'{self.api}/datasets/{id}/stats/'
        data = self._get_request(url)
        data = self._pretty_response(ast.literal_eval(data))
        return data

    def excel(self, id, filepath):
        url = f'{self.api}/datasets/{id}/excel/'
        data = requests.get(url)
        open(filepath, 'wb').write(data.content)

    def pdf(self, id, filepath):
        url = f'{self.api}/datasets/{id}/plot/'
        data = requests.get(url)
        open(filepath, 'wb').write(data.content)


    def delete_dataset(self, id):
        url = f'{self.api}/datasets/{id}/'
        data = self._delete_dataset(url)
        return data

    def _get_request(self, url: str) -> Any:
        data = requests.get(url)
        resp = self._handle_data(data)
        return resp

    def _pretty_response(self, data):
        return json.dumps(data, indent=4, sort_keys=True)

    def _parse_json(self, content: str):
        json_res = json.loads(content)
        return json_res

    def _post_request(self, url, filename):
        files = {'file': open(filename, 'rb')}
        data = requests.post(url, files=files)
        resp = self._handle_data(data)
        return resp

    def _delete_dataset(self, url):
        data = requests.delete(url)
        resp = self._handle_data(data)
        return resp

    def _handle_data(self, data: Any):
        if data.status_code == 400:
            message = self._parse_json(data.content)
            print(message['message'])
            sys.exit(1)
        if data.status_code == 200:
            resp = self._parse_json(data.content)
            return resp
