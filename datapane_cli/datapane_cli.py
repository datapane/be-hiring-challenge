import argparse
from .utils import *

parser = argparse.ArgumentParser()

parser.add_argument('-ds', '--datasets', help="list datasets")
parser.add_argument('-id', '--id', help="unique identifier for a dataset", required=True)
parser.add_argument('-path', '--file path', help="where the dataset is located in your system")
parser.add_argument('-find', '--single_dataset', help="show size of single dataset", action='store_true')
parser.add_argument('-delete', '--delete', help="delete single dataset", action='store_true')
parser.add_argument('-describe', '--describe', help="describe single dataset", action='store_true')
parser.add_argument('-histogram', '--histogram', help="print histogram to pdf ", action='store_true')
parser.add_argument('-excel', '--excel', help="generate excel file of dataset", action='store_true')

args = parser.parse_args()

# evaluate parse arguments
if args.datasets:
    for id, file in enumerate(list_datasets()):
        print(f'{id} \t {file} \n')

if args.single_datset:
    print(single_dataset(args.id))

if args.delete:
    print(delete_dataset(args.id))

if args.describe:
    print(describe_dataset(args.id))

if args.excel:
    print(export_to_excel(args.id))

if args.histogram:
    print(export_to_pdf(args.id))
