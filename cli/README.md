# The quickest way to share datasets and results.

# 

## Installation

```shell script
pip install -r requirements.txt
pip install setup.py
```

Using docker [recommended]  
```shell script
make docker
docker run -it --network=host datapane:latest
```

Example
[Assuming API server is running on localhost:8000]
```shell script
docker run -it --network=host --mount type=bind,source="$(pwd)/..",target=/app,readonly datapane:latest create -f sample_data_1.csv
docker run -it --network=host --mount type=bind,source="$(pwd)/..",target=/app datapane:latest -i <id-from-response-above> plot
docker run -it --network=host --mount type=bind,source="$(pwd)/..",target=/app datapane:latest -i <id-from-response-above> excel
docker run -it --network=host datapane:latest -i <id-from-response-above> stats
```
## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run datapane cli application

$ datapane --help


### run pytest / coverage

$ make test
```


### Releasing to PyPi

Before releasing to PyPi, you must configure your login credentials:

**~/.pypirc**:

```
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```

Then use the included helper function via the `Makefile`:

```
$ make dist

$ make dist-upload
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `Datapane`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it datapane --help
```
