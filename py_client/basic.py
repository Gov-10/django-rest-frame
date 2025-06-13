import requests

endpoint = "http://127.0.0.1:8000/api"

get_requests = requests.get(endpoint, json={"query": "Test data"})
# print(get_requests.text) #prints raw text response
print(get_requests.status_code)