import requests

def get_user_data(username):
    url =f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise ValueError(f"User '{username}' not found.")
