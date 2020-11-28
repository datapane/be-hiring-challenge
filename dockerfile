FROM python:3.8-slim-buster

RUN apt update && apt install -y libpq-dev build-essential
ADD . /home/backend/

WORKDIR /home/backend/cli

RUN for x in `ls ../local_deps`; do pip install ../local_deps/$x; done

RUN python setup.py sdist bdist_wheel
RUN pip install dist/datapane_cli-0.1.0-py3-none-any.whl

WORKDIR /home/backend/api
RUN pip install -r requirements.txt

# COPY .dev.env .env
#CMD python manage.py collectstatic