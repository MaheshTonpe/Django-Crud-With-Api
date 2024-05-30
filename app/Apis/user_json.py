# import requests
# import json

# API_BASE_URL = "http://127.0.0.1:8000/api/user"

# def get_data():
#     response = requests.get(API_BASE_URL + "/list/")
#     return response.json()

# def create_data(data):
#     response = requests.post(API_BASE_URL + "/list/", data=json.dumps(data), headers={"Content-Type": "application/json"})
#     return response.json()

# def update_data(id, data):
#     response = requests.put(API_BASE_URL + f"/<int:pk>/{id}", data=json.dumps(data), headers={"Content-Type": "application/json"})
#     return response.json()

# def delete_data(id):
#     response = requests.delete(API_BASE_URL + f"/<int:pk>/{id}")
#     return response.json()
