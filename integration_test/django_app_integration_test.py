import os
import json
import requests

# Set the Django application's URL as an environment variable
DJANGO_APP_URL = os.environ.get('DJANGO_APP_URL', 'http://localhost:8000')

dir_path = os.path.dirname(os.path.realpath(__file__))

# Create a test CSV file
csv_file_path = f'{dir_path}/../data/seattle-weather.csv'

# Upload the CSV file
with open(csv_file_path, 'rb') as file:
    upload_url = f'{DJANGO_APP_URL}/api/upload/'
    response = requests.post(upload_url, files={'csv_file': file})
    print(f'Upload Response: {response.status_code}')

# Query data with a specific filter
query_url = f'{DJANGO_APP_URL}/api/query/?weather=sun'
response = requests.get(query_url)
print(f'Query Response: {response.status_code}')
data = json.loads(response.content)
print(f'Query Result: {data}')
assert len(data) == 640

# Query data with a specific filter
query_url = f'{DJANGO_APP_URL}/api/query/?weather=rain'
response = requests.get(query_url)
print(f'Query Response: {response.status_code}')
data2 = json.loads(response.content)
print(f'Query Result: {data2}')
assert len(data2) == 641

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
