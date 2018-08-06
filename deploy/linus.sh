#!/usr/bin/env bash

cd /home/linus/linus

exec /home/linus/.virtualenvs/linus/bin/gunicorn config.wsgi -b 127.0.0.1:8001 -w 3 --timeout 1000