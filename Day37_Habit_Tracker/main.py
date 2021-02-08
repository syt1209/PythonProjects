import requests
from datetime import datetime

USERNAME = "ys2021"
TOKEN = "abcdefghij"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPHID = "graph1"
graph_config = {
    "id": GRAPHID,
    "name": "Python Coding",
    "unit": "min",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

graph_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now()

pixel_config ={
    "date": today.strftime("%Y%m%d"),
    "quantity": "30",
}

response_pixel = requests.post(url=graph_pixel_endpoint, json=pixel_config, headers=headers)
print(response_pixel.text)