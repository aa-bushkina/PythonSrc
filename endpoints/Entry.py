import requests


def add_entry(token, client_id, book_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/entries"
    path = "/entry/add"
    response = requests.post(f"{url}{path}",
                             data={'clientId': client_id, 'bookId': book_id},
                             headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def get_all_entries_by_book(token, book_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/entries"
    path = "/all/by-book"
    response = requests.get(f"{url}{path}",
                            params={'bookId': book_id},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def get_all_entries_by_client(token, client_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/entries"
    path = "/all/by-client"
    response = requests.get(f"{url}{path}",
                            params={'clientId': client_id},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def get_all_entries(token):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/entries"
    path = "/all"
    response = requests.get(f"{url}{path}",
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def update_entry_data_ret(token, entry_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/entries"
    path = "/entry/update/data-ret"
    response = requests.put(f"{url}{path}",
                            data={'id': entry_id},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def delete_entry(token, entry_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/entries"
    path = "/entry/delete"
    response = requests.delete(f"{url}{path}",
                               data={'id': entry_id},
                               headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)

    return response.json()
