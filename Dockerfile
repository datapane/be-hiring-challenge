# Set base image
FROM python:3.6

# No buffer for terminal output
ENV PYTHONUNBUFFERED 1

# Setup container at datapane directory and install dependencies
RUN mkdir ./datapane
WORKDIR ./datapane
ADD . /datapane/
RUN pip install -r requirements.txt
