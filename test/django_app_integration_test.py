import os
import json
import requests

# Set the Django application's URL as an environment variable
DJANGO_APP_URL = os.environ.get('DJANGO_APP_URL', 'http://localhost:8000')

# Create a test CSV file
csv_file_path = 'test_data.csv'
test_csv_data = [
    {'date': '2023-01-01', 'precipitation': 0.0, 'temp_max': 25.0, 'temp_min': 15.0, 'wind': 5.0, 'weather': 'clear'},
    {'date': '2023-01-02', 'precipitation': 0.0, 'temp_max': 35.0, 'temp_min': 15.0, 'wind': 5.0, 'weather': 'sunny'},
    {'date': '2023-01-03', 'precipitation': 0.0, 'temp_max': 45.0, 'temp_min': 15.0, 'wind': 5.0, 'weather': 'cloudy'},
    {'date': '2023-01-04', 'precipitation': 0.0, 'temp_max': 55.0, 'temp_min': 15.0, 'wind': 5.0, 'weather': 'rain'},
    {'date': '2023-01-05', 'precipitation': 0.0, 'temp_max': 45.0, 'temp_min': 15.0, 'wind': 5.0, 'weather': 'rain'},
    # Add more test data as needed
]
with open(csv_file_path, 'w') as test_csv_file:
    test_csv_file.write('date,precipitation,temp_max,temp_min,wind,weather\n')
    for row in test_csv_data:
        test_csv_file.write(','.join(map(str, row.values())) + '\n')

# Upload the CSV file
with open(csv_file_path, 'rb') as file:
    upload_url = f'{DJANGO_APP_URL}/api/upload/'
    response = requests.post(upload_url, files={'csv_file': file})
    print(f'Upload Response: {response.status_code}')

# Query data with a specific filter
query_url = f'{DJANGO_APP_URL}/api/query/?weather=sunny'
response = requests.get(query_url)
print(f'Query Response: {response.status_code}')
data = json.loads(response.content)
print(f'Query Result: {data}')
assert len(data) == 1

# Query data with a specific filter
query_url = f'{DJANGO_APP_URL}/api/query/?weather=rain'
response = requests.get(query_url)
print(f'Query Response: {response.status_code}')
data2 = json.loads(response.content)
print(f'Query Result: {data2}')
assert len(data2) == 2

# Query data with a limit
query_url_with_limit = f'{DJANGO_APP_URL}/api/query/?limit=3'
response = requests.get(query_url_with_limit)
print(f'Query with Limit Response: {response.status_code}')
data_with_limit = json.loads(response.content)
print(f'Query with Limit Result: {data_with_limit}')
assert len(data_with_limit) == 3

# Query data with a combination of filter and limit
query_url_combined = f'{DJANGO_APP_URL}/api/query/?weather=rain&limit=1'
response = requests.get(query_url_combined)
print(f'Combined Query Response: {response.status_code}')
data_combined = json.loads(response.content)
print(f'Combined Query Result: {data_combined}')
assert len(data_combined) == 1

# Clean up the test CSV file
os.remove(csv_file_path)
