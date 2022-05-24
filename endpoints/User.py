from dataclasses import dataclass

import requests


@dataclass
class LoginResponse:
    client_id: int = None
    is_admin: bool = False
    token: str = None


def get_user(token, username):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080"
    path = "/api/user/get"
    response = requests.get(f"{url}{path}", params={'username': username}, headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def log_in(username, password):
    url = "http://localhost:8080"
    path = "/api/login"
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    response = requests.post(f"{url}{path}", data=f"username={username}&password={password}", headers=headers)
    response_text = response.text
    token = response_text[response_text.find(":\"") + 2:response_text.find("\",\"")]
    client_id = get_user(token, username)['client']['id']
    headers = {"Authorization": "Bearer " + token}
    admin_response = requests.post("http://localhost:8080/api/user/test", headers=headers)
    is_admin = False
    if admin_response.status_code == 200:
        is_admin = True
    return LoginResponse(client_id, is_admin, token)


def get_users(token):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080"
    path = "/api/users"
    response = requests.get(f"{url}{path}", headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()
