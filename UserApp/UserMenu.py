from Details import *

from prettytable import PrettyTable


def user_app(token, client_id):
    while True:
        print("Перейти: ")
        print("1 - Все книги")
        print("2 - Все жанры книг")
        print("3 - Мои записи")
        print("4 - Мои данные")
        print("0 - Выход")
        action = input()
        match action:
            case "1":
                go_to_books(token)
            case "2":
                go_to_booktypes(token)
            case "3":
                go_to_entries(token, client_id)
            case "4":
                go_to_personal_data(token, client_id)
            case "0":
                break
            case _:
                print("Некорректное действие! Выберите действие из указанных!\n")


def go_to_books(token):
    show_all_books(token)


def go_to_booktypes(token):
    booktypes = show_all_booktypes(token)
    while True:
        print("1 - Посмотреть все книги жанра")
        print("0 - Вернуться на домашнюю страницу")
        action = input()
        match action:
            case "1":
                while True:
                    print("Введите номер жанра из таблицы")
                    try:
                        num = int(input())
                        if num == 0:
                            return
                        if 0 <= num < len(booktypes):
                            show_all_books_by_booktype(token, booktypes, num)
                            break
                        else:
                            print("Некорректное число! Выберите число из указанных!\n")
                    except ValueError:
                        print("Некорректный символ! Выберите номер из указанных!\n")
            case "0":
                return
            case _:
                print("Некорректное действие! Выберите действие из указанных!\n")


def go_to_entries(token, client_id):
    entries = get_all_entries(token)
    table = PrettyTable()
    table.field_names = ['№', 'Книга', 'Дата начала', 'Дата сдачи', 'Дата конца']
    for i in range(len(entries)):
        data_beg = entries[i]['dataBeg'][:10]
        data_end = entries[i]['dataEnd'][:10]
        data_ret = entries[i]['dataRet']
        if data_ret is None:
            data_ret = ''
        if entries[i]['client']['id'] == client_id:
            table.add_row(
                [i, entries[i]['book']['name'], data_beg, data_ret, data_end])
    print(table)


def go_to_personal_data(token, client_id):
    client = get_client(token, client_id)
    print("Данные пользователя:")
    print("Фамилия: " + client['lastName'])
    print("Имя: " + client['firstName'])
    print("Отчество: " + client['patherName'])
    print("Серия паспорта: " + client['passportSeria'])
    print("Номер паспорта: " + client['passportNum'])
    print('\n')
