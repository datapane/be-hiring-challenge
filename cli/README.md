# datapane-cli
## Command line client

Simple command line client developed in [click](https://pypi.org/project/click/)

## Dependencies

- [click](https://pypi.org/project/click/)
- [requests](https://pypi.org/project/requests/)

## Installation

  ```bash
    pip install -e cli
  ```

## Usage

### Upload a dataset
  ```bash
    datapane-cli import --file <file path> [--title] <title>
  ```

  **Options:**
* `-f --file`: CSV file path for the dataset to be uploaded
* `-t --title`: Title for the uploaded dataset

### Download a dataset
  ```bash
    datapane-cli export --id <id> [--action] <action>
  ```

  **Options:**
* `--id`: ID for the dataset to be downloaded
* `-a --action`: Action for export (default: view name and size, `plot`: get histogram PDF, `excel`: download as XLSX)

### Delete a dataset
  ```bash
    datapane-cli delete --id <id>
  ```

  **Options:**
* `--id`: ID for the dataset to be deleted

### List all datasets
  ```bash
    datapane-cli ls
  ```
