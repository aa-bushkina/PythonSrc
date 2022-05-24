from AdminApp.BookActions import *
from AdminApp.BooktypeActions import *
from AdminApp.EntryActions import *
from AdminApp.ClientActions import *


def admin_app(token):
    while True:
        print("Перейти: ")
        print("1 - Раздел книг")
        print("2 - Раздел жанров книг")
        print("3 - Журнал записей")
        print("4 - Раздел клиентов")
        print("0 - Выход")
        action = input()
        match action:
            case "1":
                go_to_books(token)
            case "2":
                go_to_booktypes(token)
            case "3":
                go_to_entries(token)
            case "4":
                go_to_clients(token)
            case "0":
                break
            case _:
                print("Некорректное действие! Выберите действие из указанных!")


def go_to_books(token):
    show_all_books(token)
    while True:
        print("1 - Добавить книги")
        print("2 - Удалить книги")
        print("3 - Посмотреть список книг")
        print("0 - Вернуться назад")
        action = input()
        match action:
            case "1":
                add_book_in_table(token)
            case "2":
                delete_book_from_table(token)
            case "3":
                show_all_books(token)
            case "0":
                return
            case _:
                print("Некорректное действие! Выберите действие из указанных!")


def go_to_booktypes(token):
    show_all_booktypes(token)
    while True:
        print("1 - Добавить жанр книги")
        print("2 - Удалить жанр книги")
        print("3 - Обновить штраф у жанра")
        print("4 - Обновить количество дней у жанра")
        print("5 - Посмотреть все книги жанра")
        print("6 - Посмотреть список жанров книг")
        print("0 - Вернуться назад")
        action = input()
        match action:
            case "1":
                add_booktype_in_table(token)
            case "2":
                delete_booktype_from_table(token)
            case "3":
                update_booktype_fine_in_table(token)
            case "4":
                update_booktype_day_count_in_table(token)
            case "5":
                show_all_books_by_booktype_in_table(token)
            case "6":
                show_all_booktypes(token)
            case "0":
                return
            case _:
                print("Некорректное действие! Выберите действие из указанных!")


def go_to_entries(token):
    show_all_entries(token)
    while True:
        print("1 - Добавить запись")
        print("2 - Удалить запись")
        print("3 - Обновить дату возвращения")
        print("4 - Посмотреть все записи по книге")
        print("5 - Посмотреть все записи по клиенту")
        print("6 - Посмотреть все записи")
        print("0 - Вернуться назад")
        action = input()
        match action:
            case "1":
                add_entry_in_table(token)
            case "2":
                delete_entry_from_table(token)
            case "3":
                update_entry_data_ret_in_table(token)
            case "4":
                show_all_entries_by_book(token)
            case "5":
                show_all_entries_by_client(token)
            case "6":
                show_all_entries(token)
            case "0":
                return
            case _:
                print("Некорректное действие! Выберите действие из указанных!")


def go_to_clients(token):
    show_all_clients(token)
    while True:
        print("1 - Добавить клиента")
        print("2 - Удалить клиента")
        print("3 - Обновить имя у клиента")
        print("4 - Обновить фамилию у клиента")
        print("5 - Обновить паспорт у клиента")
        print("6 - Посмотреть список клиентов")
        print("0 - Вернуться назад")
        action = input()
        match action:
            case "1":
                add_client_in_table(token)
            case "2":
                delete_client_from_table(token)
            case "3":
                update_client_firstname_in_table(token)
            case "4":
                update_client_lastname_in_table(token)
            case "5":
                update_client_passport_in_table(token)
            case "6":
                show_all_clients(token)
            case "0":
                return
            case _:
                print("Некорректное действие! Выберите действие из указанных!")
