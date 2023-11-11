FROM python:3.10-slim-bullseye

ADD requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

ADD src/ /src/
ADD scripts/ /scripts/

WORKDIR /src

# Sets a default admin password for local testing
ENV DJANGO_SUPERUSER_PASSWORD "admin"
ENV DJANGO_SETTINGS_MODULE "CsvToJsonApi.settings"
ENV PYTHONPATH "${PYTHONPATH}:/src"

# Create the database tables through the django migrations
RUN python manage.py migrate

# Run unit tests
RUN python manage.py test CsvToJsonApi/tests

# Expose the port in which it runs. 
EXPOSE 8000

CMD ["/scripts/run_server.sh"]
