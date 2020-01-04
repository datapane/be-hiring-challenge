## Datapane CLI

This is the tool to interact with the datapane
server which help to perform CRUD operation on it
and more.

#### Installation

Clone the repo and ``cd`` into the ``datapane_cli``
repo


```

cd datapane_cli

python3 -m venv ~/.virtualenvs/datapane_cli

workon datapane_cli

pip install --editable .

```

or 

```

cd datapane_cli

pip3 install .

```


This will install the dependency into the virtual
environment and you will be ready to play with the API.

:Note: Make sure the server is running

#### How To Use

To query all the datasets that are available:

``datapane datasets show``

To create a dataset

``datapane datasets create --filenam sample_data_1.csv``

Where `sample_data_1` is the csv file supplied

To delete a dataset

``datapane datasets delete --id 8``

To get the information about a single dataset

``datapane datasets get --id 5``

To get stats of a particular dataset

``datapane datasets stats --id``

To export the dataset to excel

``datapane datasets excel --id 5 --filename test.xlsx``

Where ``filename`` is the path to excel file

To get pdf of all the plots

``datapane datasets plot --id 5 --filename test.pdf``

Where ``filename`` is the path to pdf file