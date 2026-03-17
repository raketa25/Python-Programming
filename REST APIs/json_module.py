"""
- This is a Python script that retrieves the user's public IP address, determines their location based on that IP address, and then fetches active weather alerts for the user's state using the National Weather Service API. The script uses the `requests` library to make HTTP requests and the `json` library to format the output. If there are active weather alerts, it prints the headline and description of each alert; otherwise, it indicates that there are no alerts.

"""
import requests
import json

ip_address = requests.get('https://api.ipify.org').text

#print(ip_address)

location = requests.get(f'http://ip-api.com/json/{ip_address}').json()

state = location['region']

print(state)
print('\n')

weather = requests.get(f'https://api.weather.gov/alerts/active?area={state}').json()
#weather = requests.get(f'https://api.weather.gov/alerts/active?area=FL').json()

# print(weather)
# print('\n')

weather_pretty = json.dumps(weather, indent=2)

# print(weather_pretty)

print(weather['features'][0]['properties']['headline'])
print(weather['features'][0]['properties']['description'])

try: 
    print('WEATHER')

    for x in weather['features']:
        print('\n --- >>>WARNING!!! <<< ---')
        print(x['properties']['headline'])
        print(x['properties']['description'])
except:
    print('No Alerts')