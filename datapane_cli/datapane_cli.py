import argparse

# help flag provides flag help
# store_true actions stores argument as True

parser = argparse.ArgumentParser()

parser.add_argument('-ds', '--datasets', help="list datasets")
parser.add_argument('-id', '--id', help="unique number for a dataset")
parser.add_argument('-path', '--file path', help="where the dataset is located in your system")
parser.add_argument('-find', '--single_dataset', help="show size of single dataset")
parser.add_argument('-ds', '--datasets', help="delete single dataset")
parser.add_argument('-describe', '--describe', help="describe single dataset")
parser.add_argument('-histogram', '--histogram', help="print histogram to pdf ")
parser.add_argument('-excel', '--excel', help="generate excel file of dataset")

args = parser.parse_args()