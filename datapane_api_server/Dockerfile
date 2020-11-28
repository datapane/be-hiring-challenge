FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

RUN mkdir /app
COPY . /app/
WORKDIR /app



RUN pip install --upgrade cython && \
    pip install --upgrade numpy && \
    pip install --upgrade pandas && \
    pip install --upgrade matplotlib && \
    pip install --upgrade pip && \
     pip install -r requirements.txt


EXPOSE $PORT
CMD python manage.py runserver 0.0.0.0:$PORT