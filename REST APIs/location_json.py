"""
- This code retrieves the public IP address of the machine running the script using the `requests` library to make a GET request to 'https://api.ipify.org'. It then uses this IP address to fetch location information from the 'http://ip-api.com/json/{ip_address}' API. The location information is printed in JSON format, and specific details about the city and state are extracted and displayed in a formatted string.

"""
import requests

ip_address = requests.get('https://api.ipify.org').text

location = requests.get(f'http://ip-api.com/json/{ip_address}').json()

print(ip_address)
print('\n')
print(location)

print(f"City:{location['city']} -- State: {location['regionName']}")