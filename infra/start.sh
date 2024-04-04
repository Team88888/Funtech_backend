#!/bin/bash

if [ "$DEBUG"==True ]; then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic --no-input

    if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
        python manage.py createsuperuser \
            --no-input \
            --username $DJANGO_SUPERUSER_USERNAME \
            --email $DJANGO_SUPERUSER_EMAIL
    fi
fi

gunicorn funtech_proj.wsgi:application --bind 0:8000
