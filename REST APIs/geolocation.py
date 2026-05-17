import requests

ip_address = requests.get('http://api.ipify.org').text

print(ip_address)

response = requests.get(f'http://ip-api.com/json/{ip_address}').json()

print(response)

print(response['city'])