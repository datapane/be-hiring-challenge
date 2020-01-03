import json
import click
import pandas as pd

import requests


HOST = '127.0.0.1'
PORT = '8000'
BASE_URL = 'http://{}:{}/datasets/'.format(HOST, PORT)

@click.group()
def cli():
    """
        Command line client group for API endpoints
    """

@cli.command('import')
@click.option('-f',
              '--file',
              required=True,
              prompt=False,
              type=click.Path(exists=True, readable=True),
              help='Dataset file path')
@click.option('-t',
              '--title',
              required=True,
              prompt=False,
              type=str,
              help='Dataset title')
def add_dataset(file, title):
    """
        Create endpoint (import dataset)
    """
    data = { 'title': title }
    files = {'csv_data': open(file, 'rb')}
    response = requests.post(BASE_URL, data=data, files=files)
    if str(response.status_code)[:2] == '20':
           print('ID of the new dataset: {}'.format(response.json()['id']))
    else:
        click.echo('Status code: {} Cannot add requested dataset'.format(response.status_code))

@cli.command('delete')
@click.option('--id',
              prompt=False,
              type=int,
              help='Dataset ID to be deleted')
def delete_dataset(id):
    """
        Delete endpoint (delete dataset)
    """
    request_url = BASE_URL + str(id)
    response = requests.delete(request_url)
    if str(response.status_code)[:2] == '20':
           print('ID of the deleted dataset: {}'.format(id))
    else:
        click.echo('Status code: {} Cannot delete requested dataset'.format(response.status_code))

@cli.command('export')
@click.option('--id',
              prompt=False,
              type=int,
              help='Dataset ID to be exported')
@click.option('-a',
              '--action',
              prompt=False,
              type=str,
              help='Type of export: plot, stats, excel')
def export_dataset(id, action):
    """
        Retrieve endpoint (based on actions)
    """
    if action is None:
        export_dataset(id)
    elif action == 'plot':
        export_plot(id)
    elif action == 'stats':
        export_stats(id)
    elif action == 'excel':
        export_excel(id)

def export_dataset(id):
    request_url = BASE_URL + str(id)
    response = requests.get(request_url)
    if str(response.status_code)[:2] == '20':
        click.echo(response.json())
    else:
        click.echo('Status code: {} Cannot access dataset'.format(response.status_code))

def export_plot(id):
    request_url = BASE_URL + '{}/plot'.format(str(id))
    response = requests.get(request_url)
    if str(response.status_code)[:2] == '20':
        filename = 'plot_{}.pdf'.format(id)
        with open(filename, 'wb') as f:
            f.write(response.content)
        click.echo('Plot for dataset id {} has been downloaded'.format(id))
    else:
        click.echo('Status code: {} Cannot access dataset'.format(response.status_code))

def export_stats(id):
    request_url = BASE_URL + '{}/stats'.format(str(id))
    response = requests.get(request_url)
    if str(response.status_code)[:2] == '20':
        click.echo(response.json())
    else:
        click.echo('Status code: {} Cannot access dataset'.format(response.status_code))

def export_excel(id):
    request_url = BASE_URL + '{}/excel'.format(str(id))
    response = requests.get(request_url)
    if str(response.status_code)[:2] == '20':
        filename = 'excel_{}.xlsx'.format(id)
        with open(filename, 'wb') as f:
            f.write(response.content)
        click.echo('Excel for dataset id {} has been downloaded'.format(id))
    else:
        click.echo('Status code: {} Cannot access dataset'.format(response.status_code))

@cli.command('ls')
def list_all_datasets():
    """
        Retrieve endpoint (list all datasets)
    """
    request_url = BASE_URL
    response = requests.get(request_url)
    if str(response.status_code)[:2] == '20':
        for dataset in response.json():
            del dataset['dataframe']
            click.echo(dataset)
    else:
        click.echo('Status code: {} Cannot access dataset list'.format(response.status_code))
