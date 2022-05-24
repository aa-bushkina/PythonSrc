import requests


def add_book(token, name, cnt, booktype_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/books"
    path = "/book/add"
    response = requests.post(f"{url}{path}",
                             data={'name': name, 'cnt': cnt, 'type_id': booktype_id},
                             headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def get_all_books_by_booktype(token, booktype_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/books"
    path = "/all/by-booktype"
    response = requests.get(f"{url}{path}",
                            params={'id': booktype_id},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def get_all_books(token):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/books"
    path = "/all"
    response = requests.get(f"{url}{path}",
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def get_book(token, book_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/books"
    path = "/book/get"
    response = requests.get(f"{url}{path}",
                            params={'id': book_id},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def update_book_cnt(token, book_id, cnt):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/books"
    path = "/book/update/cnt"
    response = requests.put(f"{url}{path}",
                            data={'id': book_id, 'cnt': cnt},
                            headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()


def delete_book(token, book_id):
    headers = {"Authorization": "Bearer " + token}
    url = "http://localhost:8080/books"
    path = "/book/delete"
    response = requests.delete(f"{url}{path}",
                               data={'id': book_id},
                               headers=headers)
    if response.status_code != 200:
        raise Exception(response.text)
    return response.json()
