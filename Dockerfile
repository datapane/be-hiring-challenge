FROM python:3.7-slim

WORKDIR /datapane

COPY . .

RUN pip install -r requirements.txt

WORKDIR /datapane/api_server

EXPOSE 8000
