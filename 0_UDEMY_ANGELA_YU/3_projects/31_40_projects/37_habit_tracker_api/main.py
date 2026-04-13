import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = "ljid048659LKOIJIklusd8UID3"
PIXELA_USERNAME = "samhayder"
GRAPH_ID = "samgraph1"

today = datetime.now()

# Create your user account
user_config = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT,json=user_config)
# print(response.text)

#Create a graph definition
GRAPHS_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
#https://pixe.la/v1/users/samhayder/graphs/samgraph1.html

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Swimming Graph",
    "unit": "5 Km",
    "type": "float",
    "color": "ajisai"
}

graph_response = requests.post(url=GRAPHS_ENDPOINT,json=graph_config,headers=headers)
# print(graph_response.text)

# Post value to the graph
POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you swimming today? ")
}

post_response = requests.post(url=POST_ENDPOINT,json=post_config,headers=headers)
print(post_response.text)