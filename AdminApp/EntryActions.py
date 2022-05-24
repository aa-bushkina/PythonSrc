from Details import *


def add_entry_in_table(token):
    while True:
        show_all_clients(token)
        print("Выберите номер клиента: ")
        try:
            client_num = int(input())
            if 0 <= client_num < len(get_all_clients(token)):
                client_id = get_all_clients(token)[client_num]['id']
                break
            print("Некорректный номер! Выберите номер из указанных!\n")
        except ValueError:
            print("Некорректный символ! Выберите номер из указанных!\n")
    while True:
        show_all_books(token)
        print("Выберите номер книги: ")
        try:
            book_num = int(input())
            if 0 <= book_num < len(get_all_books(token)):
                book_id = get_all_books(token)[book_num]['id']
                break
            print("Некорректный номер! Выберите номер из указанных!\n")
        except ValueError:
            print("Некорректный символ! Выберите номер из указанных!\n")
    try:
        add_entry(token, client_id, book_id)
        print("Запись успешно добавлена\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")


def delete_entry_from_table(token):
    while True:
        show_all_entries(token)
        print("Выберите номер записи: ")
        try:
            entry_num = int(input())
            if 0 <= entry_num < len(get_all_entries(token)):
                entry_id = get_all_entries(token)[entry_num]['id']
                break
            print("Некорректный номер! Выберите номер из указанных!\n")
        except ValueError:
            print("Некорректный символ! Выберите номер из указанных!\n")
    try:
        delete_entry(token, entry_id)
        print("Запись успешно удалена\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")


def update_entry_data_ret_in_table(token):
    while True:
        show_all_entries(token)
        print("Выберите номер записи: ")
        try:
            entry_num = int(input())
            if 0 <= entry_num < len(get_all_entries(token)):
                entry_id = get_all_entries(token)[entry_num]['id']
                break
            print("Некорректный номер! Выберите номер из указанных!\n")
        except ValueError:
            print("Некорректный символ! Выберите номер из указанных!\n")
    try:
        update_entry_data_ret(token, entry_id)
        print("Дата возврата успешно обновлена\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")


def show_all_entries_by_book(token):
    while True:
        show_all_books(token)
        print("Выберите номер книги: ")
        try:
            book_num = int(input())
            if 0 <= book_num < len(get_all_books(token)):
                book_id = get_all_books(token)[book_num]['id']
                break
            print("Некорректный номер! Выберите номер из указанных!\n")
        except ValueError:
            print("Некорректный символ! Выберите номер из указанных!\n")
    entries = get_all_entries(token)
    table = PrettyTable()
    table.field_names = ['№', 'Книга', 'Клиент', 'Дата начала', 'Дата сдачи', 'Дата конца']
    num = 0
    for i in range(len(entries)):
        data_beg = entries[i]['dataBeg'][:10]
        data_end = entries[i]['dataEnd'][:10]
        data_ret = entries[i]['dataRet']
        if data_ret is None:
            data_ret = ""
        else:
            data_ret = data_ret[:10]
        if entries[i]['book']['id'] == book_id:
            table.add_row([num, entries[i]['book']['name'],
                           entries[i]['client']['lastName'] + ' ' + entries[i]['client']['firstName'] + ' ' +
                           entries[i]['client']['patherName'], data_beg, data_ret, data_end])
            num = num + 1
    print(table)


def show_all_entries_by_client(token):
    while True:
        show_all_clients(token)
        print("Выберите номер клиента: ")
        try:
            client_num = int(input())
            if 0 <= client_num < len(get_all_clients(token)):
                client_id = get_all_clients(token)[client_num]['id']
                break
            print("Некорректный номер! Выберите номер из указанных!\n")
        except ValueError:
            print("Некорректный символ! Выберите номер из указанных!\n")
    entries = get_all_entries(token)
    table = PrettyTable()
    table.field_names = ["№", "Клиент", "Книга", "Дата начала", "Дата сдачи", "Дата конца"]
    num = 0
    for i in range(len(entries)):
        data_beg = entries[i]['dataBeg'][:10]
        data_end = entries[i]['dataEnd'][:10]
        data_ret = entries[i]['dataRet']
        if data_ret is None:
            data_ret = ""
        else:
            data_ret = data_ret[:10]
        if entries[i]['client']['id'] == client_id:
            table.add_row([num, entries[i]['client']['lastName'] + ' ' + entries[i]['client']['firstName'] + ' ' +
                           entries[i]['client']['patherName'], entries[i]['book']['name'], data_beg,
                           data_ret, data_end])
            num = num + 1
    print(table)
