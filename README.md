# Backend API Hiring Challenge

## Prequisites

* Python3.8
* Docker

## Installation

### API
Using Docker run these commands:
* `cd <git_repo>`
* `sudo docker-compose build`
* `sudo docker-compose up`

### CLI Tool
You can run the cli tool with ease just have to export a save location(folder) like this `export DT_TARGET=<save_location>` for saving db and feather files.
Now You can either install or run directly with `python commands/commands.py --help`

To install:

* `python setup.py sdist bdist_wheel`
* `pip install dist/datapane_cli-0.1.0-py3-none-any.whl` 
* `dataplane --help`

### Instructions

#### API
You can use swagger at localhost:8000/swagger or redoc at localhost:8000/redoc to check apis

### CLI
Helpers here 

* `datapane upload <csv_file>`
* `datapane get all`
* `datapane get 1`
* `datapane generate-plot 1 test/test.pdf`
* `datapane to-excel 1 test/test.xls`
* `datapane generate-stats 1`