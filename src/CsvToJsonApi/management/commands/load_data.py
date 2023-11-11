import csv
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.db import connection, models
from CsvToJsonApi.models import WeatherData

class Command(BaseCommand):
    help = 'Load data from CSV file into the database or overwrite the existing data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        # Read the header of the CSV file to dynamically create the model
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)

        # Clear existing data in the table
        WeatherData.objects.all().delete()

        # Load data from the CSV file
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                dynamic_data = WeatherData(**row)
                dynamic_data.save()

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
