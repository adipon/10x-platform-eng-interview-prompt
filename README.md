## 10x Genomics Platform Engineering Technical Coding Prompt

Create a web service that converts a CSV file into an API that exposes JSON.

We've provided a CSV file of Seattle weather in
[`seattle-weather.csv`](./data/seattle-weather.csv). It contains the following
labels in the header, with the following format:

```
date,precipitation,temp_max,temp_min,wind,weather
...
2012-06-03,0.0,17.2,9.4,2.9,sun
2012-06-04,1.3,12.8,8.9,3.1,rain
...
```

## Prerequisites

This application requires that the following be installed on the build environment:

1. Python 3.10
2. Docker

## Building and Running

### Building docker images of the application

Docker images for the application and the API tester can be accomplished by running the following command from the project root dir:

`scripts/build_all_docker_images.sh`

### Running the web service from within a Docker container

The Django web application can be run from within a Docker container by running the following command from the project root dir:

`scripts/run_server_in_docker.sh`

This web service will be available in browsers and other clients at `localhost:8000` by default.

### Running the web service locally

The Django web application can be run on your local machine by running the following commands from the project root dir:

```
pip install -r requirements.txt
scripts/run_server_in_docker.sh
```

This web service will be available in browsers and other clients at `localhost:8000` by default.

### Running the integration tests

The API integration tests can be run either locally or from within a docker client using the following commands, repsectively:

```
pip install requests
scripts/run_integration_tests.sh
```

`scripts/run_integration_tests_in_docker.sh`

The integration tests loads the Seattle weather data located at `scripts/seattle-weather.csv` and the queries the web service for using different attributes of the data. 

## API Endpoints

The web service currently exposes two api endpoints `/api/upload/` (POST) and `/api/query/` (GET)

### `/api/upload/` Endpoint 

This endpoint allows for the upload of a CSV file containing weather data to be sent to the server. This CSV file will be processed and will perform a complete replacement of existing data in the database. In future iterations, it is highly recommended to allow this capability to a restricted set of authorized users. 

This operation can also be executed using the following command:

`python manage.py load_data /path/to/csv/file`

### `/api/query/` Endpoint

This endpoint allows for querying of data while filtering on different attributes and limiting the size of the returned dataset. All output is returned as a JSON list of WeatherData objects. Some examples of available queries for a server running in the docker container are:

`localhost:8000/api/query/?weather=rain`

`localhost:8000/api/query/?limit=3`

`localhost:8000/api/query/?weather=rain&limit=1`

Future work would add pagination to the results for easier processing of the data by clients.
