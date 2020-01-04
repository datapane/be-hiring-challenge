# Dataset Command Line Tool

This is a API client command line python application for Dataset API.

## Requirements

Be sure you have the following installed on your development machine:

+ Python >= 3.6.4
+ setuptools >= 44.0.0 
+ Click==7.0
+ requests==2.22.0


## Install Dataset-cli:

```bash
pip install -e dataset-cli
```

## Dataset-cli Actions:

List All Datasets:
```bash
dataset-cli list
```

Create Dataset:
```bash
dataset-cli create -f /path/to/csv/file.csv
```

Retrieve Dataset:
```bash
dataset-cli get <dataset_id>
```

Retrieve Dataset Stats:
```bash
dataset-cli stats <dataset_id>
```

Delete Dataset:
```bash
dataset-cli delete <dataset_id>
```

Export Dataset to Excel:
```bash
dataset-cli excel <dataset_id>
```

Export Dataset histogram plot to PDF:
```bash
dataset-cli plot <dataset_id>
```
