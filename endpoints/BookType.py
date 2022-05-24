import requests


def add_booktype(token, name, fine, day_count):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/booktypes"
    path = "/booktype/add"
    response = requests.post(f"{url}{path}",
                             data={'name': name, 'fine': fine, 'day_count': day_count},
                             headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def get_all_booktypes(token):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080"
    path = "/booktypes/all"
    response = requests.get(f"{url}{path}",
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def get_booktype(token, booktype_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080"
    path = "/booktypes/booktype/get"
    response = requests.get(f"{url}{path}",
                            params={'id': booktype_id},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def update_booktype_cnt(token, booktype_id, cnt):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080"
    path = "/booktypes/booktype/update/cnt"
    response = requests.put(f"{url}{path}",
                            data={'id': booktype_id, 'cnt': cnt},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def update_booktype_fine(token, booktype_id, fine):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080"
    path = "/booktypes/booktype/update/fine"
    response = requests.put(f"{url}{path}",
                            data={'id': booktype_id, 'fine': fine},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def update_booktype_day_count(token, booktype_id, day_count):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080"
    path = "/booktypes/booktype/update/daycount"
    response = requests.put(f"{url}{path}",
                            data={'id': booktype_id, 'day_count': day_count},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def delete_booktype(token, booktype_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080"
    path = "/booktypes/booktype/delete"
    response = requests.delete(f"{url}{path}",
                               data={'id': booktype_id},
                               headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()
