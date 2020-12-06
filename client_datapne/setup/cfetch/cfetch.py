#!/usr/bin/env python

import os
from urllib.parse import urljoin
import argparse
import sys

import requests


class CFClient():
    """
    """

    def __init__(self, timeout=10):
        self.timeout = timeout
        if not os.getenv('CFETCH_SERVER'): 
            raise Exception('Please set CFETCH_SERVER env variable')
        self.server = os.getenv('CFETCH_SERVER')

    def format_output(self, response):
        print(response.url)
        print(response.status_code)
        print(response.text)

    def get_datasets(self, dataset_id=None):
        url = urljoin(self.server, '/datasets/')
        url = urljoin(url, str(dataset_id)) if dataset_id else url
        return self.format_output(requests.get(url, timeout=self.timeout))      

    def upload_dataset(self, filepath):
        url = urljoin(self.server, '/datasets/')
        files = {'upload_file': open(filepath, 'rb')}
        return self.format_output(requests.post(url, files=files, data={}, timeout=self.timeout))
 
    def delete_dataset(self, dataset_id):
        if not dataset_id:
            raise Exception('pass dataset_id')
        url = urljoin(self.server, '/datasets/'+str(dataset_id))
        return self.format_output(requests.delete(url, timeout=self.timeout))

    def stats(self, dataset_id):
        if not dataset_id:
            raise Exception('pass dataset_id')
        url = urljoin(self.server, '/datasets/'+str(dataset_id)+'/stats/')
        return self.format_output(requests.get(url, timeout=self.timeout))

    def plot(self, dataset_id):
        if not dataset_id:
           raise Exception('pass dataset_id')
        url = urljoin(self.server, '/datasets/'+str(dataset_id)+'/plot/')
        return self.format_output(requests.get(url, timeout=self.timeout))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='standalone client for cfetch server',
            usage='''cfetch.py <command> [<args>]
            commands are:
		   get_datasets
		   upload_dataset
		   delete_dataset
		   stats
		   plot
		''')

    parser.add_argument('command', help='Subcommand to run')
    args = parser.parse_args(sys.argv[1:2])
    client = CFClient(timeout=5)
    if not hasattr(client, args.command):
        print('Unrecognized command')
        parser.print_help()
        exit(1)
    getattr(client, args.command)(sys.argv[2]) if len(sys.argv)>2 else getattr(client, args.command)()


