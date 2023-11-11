import os
from django.core.management import call_command
from django.test import TestCase
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from CsvToJsonApi.models import WeatherData

class LoadDataTestCase(TestCase):
    def setUp(self):
        self.csv_file_path = './test-data.csv'
        self.csv_data = [
            {'date': '2023-01-01', 'precipitation': 0.0, 'temp_max': 25.0, 'temp_min': 15.0, 'wind': 5.0, 'weather': 'clear'},
            {'date': '2023-01-02', 'precipitation': 0.0, 'temp_max': 35.0, 'temp_min': 15.0, 'wind': 5.0, 'weather': 'sunny'},
            {'date': '2023-01-03', 'precipitation': 0.0, 'temp_max': 45.0, 'temp_min': 15.0, 'wind': 5.0, 'weather': 'cloudy'},
            # Add more test data as needed
        ]

    def tearDown(self):
        # Clean up the test database
        WeatherData.objects.all().delete()

    def test_load_data_command(self):
        # Save test CSV data to a temporary file
        with open(self.csv_file_path, 'w') as csv_file:
            csv_file.write('date,precipitation,temp_max,temp_min,wind,weather\n')
            for row in self.csv_data:
                csv_file.write(','.join(map(str, row.values())) + '\n')

        # Call the management command to load data
        call_command('load_data', self.csv_file_path)

        # Check if data is loaded successfully
        loaded_data = WeatherData.objects.all()
        self.assertEqual(len(loaded_data), len(self.csv_data))
        for i, row in enumerate(self.csv_data):
            for key, value in row.items():
                self.assertEqual(getattr(loaded_data[i], key), value)

        # Clean up the temporary file
        os.remove(self.csv_file_path)
