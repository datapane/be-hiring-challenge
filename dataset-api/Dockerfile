# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# Install dependencies

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml /code/
RUN poetry install
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
COPY . /code/
RUN chown -R $USER:$USER .
