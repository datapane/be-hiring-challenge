import requests


class Service:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.base = "http://{}:{}/api".format(self.host, self.port)

    def list(self):
        return requests.get("{}/datasets/".format(self.base)).json()

    def create(self, file):
        return requests.post("{}/datasets/".format(self.base), files=file).json()

    def view(self, id):
        return requests.get("{}/datasets/{}/".format(self.base, id)).json()

    def delete(self, id):
        return requests.delete("{}/datasets/{}/".format(self.base, id)).status_code == 204

    def excel(self, id):
        return requests.get("{}/datasets/{}/excel/".format(self.base, id))

    def stats(self, id):
        return requests.get("{}/datasets/{}/stats/".format(self.base, id)).json()

    def plot(self, id):
        return requests.get("{}/datasets/{}/plot/".format(self.base, id))
