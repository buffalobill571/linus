#!/usr/bin/env bash

cd /home/richard/linus

exec /home/richard/.virtualenvs/richard/bin/gunicorn config.wsgi -b 127.0.0.1:8000 -w 3 --timeout 1000
