import requests
from datetime import datetime

# Constants
USERNAME = "raketa25"
TOKEN = "ZpmConsult$25"
GRAPH_ID = "graph07"

# API Endpoints
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create User
response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
print(response.text)
print("\n")

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response2.text)
print("\n")

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2026, month=5, day=18).strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("How many commits did you make today? "),
    # "optionalData": "{\"key\": \"value\"}"
}

response3 = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response3.text)