import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users'

dummy_data = []

for i in range(10):
    response = requests.get(API_URL).json()
    
    user_name = response[i]['username']
    user_company_name = response[i]['company']['name']
    user_lat = response[i]['address']['geo']['lat']
    if float(user_lat) < 80 and float(user_lat) > -80:
        user_lat_pass = user_lat
    else:
        user_lat_pass = None
    user_lng = response[i]['address']['geo']['lng']
    if float(user_lng) < 80 and float(user_lng) > -80:
        user_lng_pass = user_lng
    else:
        user_lng_pass = None

    user = {
        'name' : user_name,
        'lng' : user_lng_pass,
        'lat' : user_lat_pass,
        'company' :user_company_name 
    }
    dummy_data.append(user)
    
print(dummy_data)
    