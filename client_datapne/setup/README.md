
### Installation
```sh
$cd client_setup/setup/
$ pip install .
```
### Usage
```sh
$ export CFETCH_SERVER=http://localhost:8080
$ cfetch.py --help
$ cfetch.py get_datasets
$ cfetch.py get_datasets <dataset_id>
$ cfetch.py upload_dataset <filepath>
$ cfetch.py delete_dataset <dataset_id>
$ cfetch.py stats <dataset_id>
$ cfetch.py plot <dataset_id>
```
### Remove package
```sh
$ pip uninstall cfetch
``
