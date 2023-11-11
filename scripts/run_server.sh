#!/bin/sh
BASEDIR=$(dirname $0)
SRCDIR=$BASEDIR/../src
cd $SRCDIR

export DJANGO_SETTINGS_MODULE="CsvToJsonApi.settings"

python manage.py runserver 0.0.0.0:8000