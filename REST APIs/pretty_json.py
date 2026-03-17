"""
-This code uses the `requests` library to fetch the user's public IP address and then retrieves the geographical location associated with that IP address using the `ip-api.com` service. The location information is printed in a pretty JSON format with indentation for better readability. Additionally, the city name from the location data is printed separately before displaying the entire JSON object.

"""
import requests
import json

ip_address = requests.get('https://api.ipify.org').text

location = requests.get(f'http://ip-api.com/json/{ip_address}').json()

print(location)
print('\n')

# Just to make the output more readable, we can use the json.dumps() function to format the JSON data with indentation. But we can not access the data in the JSON object if we convert it to a string using json.dumps(). So we will print the city name before converting it to a pretty JSON string.
location_pretty = json.dumps(location, indent=2)

print(location['city'])
print('\n')
print(location_pretty)