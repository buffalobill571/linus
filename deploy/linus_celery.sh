#!/usr/bin/env bash

cd /home/linus/linus

exec /home/linus/.virtualenvs/linus/bin/python manage.py celery worker -B
