#!/bin/sh
BASEDIR=$(dirname $0)
SRCDIR=$BASEDIR/../

echo "Build the docker container for the django server"
docker build -f docker/Dockerfile -t csvtojsonapi .

echo "Build the django container for the client tester"
docker build -f docker/Dockerfile-test -t csvtojsonapitester .

echo "Completed docker builds"