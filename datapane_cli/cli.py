import os, sys

#Following lines are for assigning parent directory dynamically.

dir_path = os.path.dirname(os.path.realpath(__file__))

parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0, parent_dir_path)

import argparse
from datapane_cli.utils import *

parser = argparse.ArgumentParser(description='File handling CLI for CSV files')

parser.add_argument('-ds', '--datasets', help="list datasets", action='store_true')
parser.add_argument('-id', '--id', help="unique identelifier for a dataset", required=True)
parser.add_argument('-upload', '--upload', help="Upload provided dataset", action='store_true')
parser.add_argument('-path', '--path', help="where the dataset is located in your system")
parser.add_argument('-find', '--single_dataset', help="show size of single dataset", action='store_true')
parser.add_argument('-delete', '--delete', help="delete single dataset", action='store_true')
parser.add_argument('-describe', '--describe', help="describe single dataset", action='store_true')
parser.add_argument('-histogram', '--histogram', help="print histogram to pdf ", action='store_true')
parser.add_argument('-excel', '--excel', help="generate excel file of dataset", action='store_true')

args = parser.parse_args()

# evaluate parse arguments
if args.datasets:
    print("<<<<<<<<<<<<<<<<Available datasets >>>>>>>>>>>>>>>>>>>\n")
    for id, file in enumerate(list_datasets()):
        print(f'id \t{id} \t file name\t{file} \n')

elif args.single_dataset:
    print(single_dataset(int(args.id)))

elif args.upload and args.path is not None:
    print(upload_dataset(args.path))

elif args.delete:
    print(delete_dataset(int(args.id)))

elif args.describe:
    print(describe_dataset(int(args.id)))

elif args.excel:
    print(export_to_excel(int(args.id)))

elif args.histogram:
    print(export_to_pdf(int(args.id)))
