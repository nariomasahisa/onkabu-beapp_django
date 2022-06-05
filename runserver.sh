#!/bin/sh

echo "Waiting for database ..."

while ! nc -z $DJANGO_DATABASE_HOSTNAME $DJANGO_DATABASE_PORT; do
  echo "DB not ready, keep waiting..."
  sleep 0.1
done

echo "database started"

python manage.py migrate
python manage.py runserver