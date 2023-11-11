FROM PYTHON:3.11-slim-bullseye

ADD requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt

COPY src/* /src/
COPY data/* /data
WORKDIR /src

# Sets a default admin password for local testing
ENV DJANGO_SUPERUSER_PASSWORD "admin"

# Create the database tables through the django migrations
RUN python manage.py migrate

# Run unit tests
RUN python manage.py test CsvToJsonApi.tests

# Load seattle weather as a starting point
RUN python manage.py load_data /data/seattle-weather.csv

EXPOSE 8000

CMD ["python", "manage.py"]
