#!/bin/bash

cd dataset
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
gunicorn dataset.wsgi --bind 0.0.0.0:8000
