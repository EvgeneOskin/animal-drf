#!/bin/sh

./manage.py migrate
uwsgi --http :80 --chdir "$PWD" --wsgi-file animals/wsgi.py
