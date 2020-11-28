# Datapane CLI Documentation
Main assumption made is that the storage to which the files are uploaded is a folder within the cli parent directory
The CLI ships with sample data to get started at the location 
`sample_data/sample_data_1.csv`
## CLI use
To run the cli, run the command
`pythone cli.py` on your terminal
Below are sample commands to perform basic operations
## View all arguments
`python3 cli.py -h`

## View all datasets
The id parameter is required by argparse but not by function so add any value such as `_`

` python3 cli.py -id _ -ds`

## Upload dataset
The id parameter is required by argparse but not by function so add any value such as `_`


` python3 cli.py -id _ -upload -path sample_data/sample_data_1.csv`

## View single dataset size

`python3 cli.py -id 0 -find`

## Describe single dataset
`python3 cli.py -id 0 -describe`

## Delete single dataset
`python3 cli.py -id 0 -delete`

## Export sigle dataset to Excel
`python3 cli.py -id 0 -excel`

## Export histogram of dataset to PDF

`python3 cli.py -id 0 -histogram`