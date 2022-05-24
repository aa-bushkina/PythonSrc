from prettytable import PrettyTable
from endpoints.Book import *
from endpoints.BookType import *
from endpoints.Client import *
from endpoints.Entry import *


def show_all_books(token):
    books = get_all_books(token)
    table = PrettyTable()
    table.field_names = ['№', 'Название', 'Количество', 'Жанр']
    for i in range(len(books)):
        table.add_row([i, books[i]['name'], books[i]['cnt'], books[i]['bookType']['name']])
    print(table)
    return books


def show_all_booktypes(token):
    booktypes = get_all_booktypes(token)
    table = PrettyTable()
    table.field_names = ['№', 'Название', 'Количество книг', 'Штраф', 'Срок выдачи']
    for i in range(len(booktypes)):
        table.add_row([i, booktypes[i]['name'], booktypes[i]['cnt'], booktypes[i]['fine'], booktypes[i]['dayCount']])
    print(table)
    return booktypes


def show_all_books_by_booktype(token, booktypes, num):
    books = get_all_books_by_booktype(token, booktypes[num]['id'])
    table = PrettyTable()
    table.field_names = ['№', 'Название', 'Количество', 'Жанр']
    num = 0
    for i in range(len(books)):
        table.add_row([num, books[i]['name'], books[i]['cnt'], books[i]['bookType']['name']])
        num = num + 1
    print(table)
    return books


def show_all_clients(token):
    clients = get_all_clients(token)
    table = PrettyTable()
    table.field_names = ['№', 'Фамилия', 'Имя', 'Отчество', 'Серия паспорта', 'Номер паспорта']
    for i in range(len(clients)):
        table.add_row(
            [i, clients[i]['lastName'], clients[i]['firstName'], clients[i]['patherName'], clients[i]['passportSeria'],
             clients[i]['passportNum']])
    print(table)
    return clients


def show_all_entries(token):
    entries = get_all_entries(token)
    table = PrettyTable()
    table.field_names = ['№', 'Книга', 'Клиент', 'Дата начала', 'Дата сдачи', 'Дата конца']
    for i in range(len(entries)):
        data_beg = entries[i]['dataBeg'][:10]
        data_end = entries[i]['dataEnd'][:10]
        data_ret = entries[i]['dataRet']
        if data_ret is None:
            data_ret = ""
        else:
            data_ret = data_ret[:10]
        table.add_row(
            [i, entries[i]['book']['name'],
             entries[i]["client"]['lastName'] + ' ' + entries[i]['client']['firstName'] + ' '
             + entries[i]['client']['patherName'], data_beg, data_ret, data_end])
    print(table)


def enter_quantity():
    while True:
        try:
            n = int(input())
            if n <= 0:
                print("Введено неверное значение! Введите целое положительное число\n")
            else:
                return n
        except ValueError:
            print("Некорректный символ! Введите целое положительное число\n")


def enter_word():
    while True:
        try:
            word = input()
            if word.isalpha() and len(word) <= 20:
                return word
            print("Введите строку из букв длиной меньше 20 символов\n")

        except ValueError:
            print("Введите строку из букв длиной меньше 20 символов\n")
