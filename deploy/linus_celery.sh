#!/usr/bin/env bash

cd /home/linus/linus

exec /home/linus/.virtualenvs/linus_up/bin/python manage.py celery worker
