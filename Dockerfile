FROM python:3.7-slim

WORKDIR /datapane

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
