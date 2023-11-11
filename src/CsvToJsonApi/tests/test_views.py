import json
import unittest
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from CsvToJsonApi.models import WeatherData

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_weather_data_view(self):
        # Insert some test data into the database
        WeatherData.objects.create(date='2023-01-01', precipitation=0.0, temp_max=25.0, temp_min=15.0, wind=5.0, weather='clear')
        WeatherData.objects.create(date='2023-01-02', precipitation=0.2, temp_max=22.0, temp_min=12.0, wind=8.0, weather='cloudy')

        # Make a GET request to the weather data view with a filter
        response = self.client.get('/api/query/?weather=clear')

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the correct data is returned
        filtered_data = json.loads(response.content)
        self.assertEqual(len(filtered_data), 1)
        self.assertEqual(filtered_data[0]['date'], '2023-01-01')

    def test_upload_csv_view(self):
        # Create a test CSV file
        test_csv_data = 'date,precipitation,temp_max,temp_min,wind,weather\n2023-01-03,0.0,28.0,18.0,6.0,sunny\n'
        test_csv_file = SimpleUploadedFile('test_data.csv', test_csv_data.encode(), content_type='text/csv')

        # Make a POST request to the upload view
        response = self.client.post('/api/upload/', {'csv_file': test_csv_file})

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if data is loaded successfully
        loaded_data = json.loads(response.content)
        self.assertEqual(loaded_data['message'], 'Data loaded successfully.')

        # Clean up
        test_csv_file.close()

if __name__ == '__main__':
    unittest.main()
