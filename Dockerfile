# Set base image
FROM python:3.8-slim

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /dataset-server

# Copy the current directory contents into the container at /app
COPY server/api server/
COPY server/server server/
COPY server/manage.py server/
COPY requirements.txt /dataset-server

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

