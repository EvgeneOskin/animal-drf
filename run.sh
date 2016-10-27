#!/bin/sh

./manage.py migrate --noinput
./manage.py collectstatic --noinput
uwsgi --http :80 --chdir "$PWD" --wsgi-file animals/wsgi.py --static-map '/static'="$PWD/static/"
