# Dataset CLI
A cli for interacting with the dataset API.

## Installation


Git clone this repository

### Prequisits

- Python ^3.8

Install the following
- [Poetry](https://python-poetry.org/)

` pip install poetry `


### Dependencies

- Create a virtual env for the project to avoid editing the main python installation

` python -m venv {path_to_venv} `

- Activate the virtual env :
 ` source {path_to_venv}/bin/activate `

For Windows:
 ` {path_to_venv}\Scripts\activate `

` poetry install `


The above command will install all the required dependencies.
It will also install the dataset-cli application.


## Usage

` dataset-cli --help `

The above command will display a help menu listing all the available commands for dataset-cli

To get dataset-cli command specific help:

`dataset-cli <command> --help  `

where command will be any of the dataset-cli avaliable commands.
for eg.,
    dataset-cli get --help
