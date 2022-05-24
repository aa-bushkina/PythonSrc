import requests


def add_client(token, lastname, firstname, pathername, pass_ser, pass_num):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/clients"
    path = "/client/add"
    response = requests.post(f"{url}{path}",
                             data={'lastName': lastname, 'firstName': firstname, 'patherName': pathername,
                                   'passportSer': pass_ser, 'passportNum': pass_num},
                             headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)

    return response.json()


def get_all_clients(token):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/clients"
    path = "/all"
    response = requests.get(f"{url}{path}",
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def get_client(token, client_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/clients"
    path = "/client/get"
    response = requests.get(f"{url}{path}",
                            params={'id': client_id},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def update_client_passport(token, client_id, pass_ser, pass_num):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/clients"
    path = "/client/update/passport"
    response = requests.put(f"{url}{path}",
                            data={'id': client_id, 'passportSer': pass_ser, 'passportNum': pass_num},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def update_client_firstname(token, client_id, firstname):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/clients"
    path = "/client/update/firstname"
    response = requests.put(f"{url}{path}",
                            data={'id': client_id, 'firstName': firstname},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def update_client_lastname(token, client_id, lastname):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/clients"
    path = "/client/update/lastname"
    response = requests.put(f"{url}{path}",
                            data={'id': client_id, 'lastName': lastname},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def delete_client(token, client_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/clients"
    path = "/client/delete"
    response = requests.delete(f"{url}{path}",
                               data={'id': client_id},
                               headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()
