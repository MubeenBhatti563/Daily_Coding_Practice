import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api-auth/auth/"

username = input("Enter your username: ")
password = getpass("Enter your password: ")

auth_response = requests.post(auth_endpoint, json={"username": username, "password": password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api-auth/product/"
    get_response = requests.get(endpoint, headers=headers)
    data = get_response.json()
    next_url = data['next']
    if next_url is not None:
        get_next = requests.get(next_url, headers=headers)
    print(data['results'])