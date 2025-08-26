import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users'

dummy_data = []
for i in range(10):
    response = requests.get(API_URL)
    parsed_data = response.json()
    dummy_data.append(parsed_data[i]['name'])

print(dummy_data)


