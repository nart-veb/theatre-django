#!/bin/bash

set -e

# Create base migrations
python manage.py migrate --noinput

if [[ $APP_DEBUG -eq 0 ]]; then
  echo "Production mode"
  python manage.py collectstatic --noinput
  gunicorn _project.wsgi:application --bind 0.0.0.0:8000
else
  echo "Development mode"
  python manage.py runserver 0.0.0.0:8000
fi