#!/bin/sh

python3 manage.py makemigrations

python3 manage.py migrate

gunicorn NFTCharityAuction.wsgi:application --bind 0.0.0.0:8000