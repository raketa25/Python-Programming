"""
- This is a simple example of how to use the requests library in Python to make a GET request to an API and retrieve data. In this case, we are making a GET request to the 'https://api.ipify.org' API, which returns the public IP address of the user. We then print the retrieved IP address to the console.
"""
import requests

ip_address = requests.get('https://api.ipify.org').text

print(f'My public IP address is: {ip_address}')
