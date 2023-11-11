#!/bin/sh
BASEDIR=$(dirname $0)
SRCDIR=$BASEDIR/../integration_test
cd $SRCDIR

export DJANGO_APP_URL="http://localhost:8000"
python -u django_app_integration_test.py