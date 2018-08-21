#!/usr/bin/env bash

cd /home/richard/linus

exec /home/richard/.virtualenvs/richard/bin/python manage.py celery worker
