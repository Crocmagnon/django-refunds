#!/bin/sh
pipenv run python manage.py migrate && \
pipenv run python manage.py collectstatic --noinput && \
pipenv run gunicorn refunds.wsgi -b 0.0.0.0:8000 --log-file -
