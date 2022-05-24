from Details import *


def add_booktype_in_table(token):
    print("Введите данные нового жанра")
    name = input("Название: ")
    print("Введите количество дней: ")
    day_count = enter_quantity()
    while True:
        try:
            fine = float(input("Введите штраф: "))
            if fine <= 0:
                print("Введите положительное число")
            break
        except ValueError:
            print("Введите целое положительное число")
    add_booktype(token, name, fine, day_count)
    try:
        print("Книга успешно добавлена\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")


def delete_booktype_from_table(token):
    while True:
        show_all_booktypes(token)
        print("Выберите номер жанра: ")
        booktype_num = int(input())
        if 0 <= booktype_num < len(get_all_booktypes(token)):
            booktype = get_all_booktypes(token)[booktype_num]
            try:
                delete_booktype(token, booktype['id'])
                print("Жанр успешно удален\n")
            except Exception as e:
                print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")
            break
        else:
            print("Некорректное число! Выберите число из указанных!")


def update_booktype_day_count_in_table(token):
    show_all_booktypes(token)
    while True:
        print("Выберите номер жанра")
        try:
            booktype_num = int(input())
            if 0 <= booktype_num < len(get_all_booktypes(token)):
                book_id = get_all_booktypes(token)[booktype_num]['id']
                break
            else:
                print("Некорректное число! Выберите число из указанных!")
        except ValueError:
            print("Некорректный символ! Выберите число из указанных!\n")
    print("Введите новое количество дней: ")
    day_count = enter_quantity()
    update_booktype_day_count(token, book_id, day_count)
    try:
        print("Штраф успешно изменен\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")


def update_booktype_fine_in_table(token):
    show_all_booktypes(token)
    while True:
        print("Выберите номер жанра")
        try:
            booktype_num = int(input())
            if 0 <= booktype_num < len(get_all_booktypes(token)):
                book_id = get_all_booktypes(token)[booktype_num]['id']
                break
            else:
                print("Некорректное число! Выберите число из указанных!")
        except ValueError:
            print("Некорректный символ! Выберите число из указанных!\n")
    while True:
        try:
            fine = float(input("Введите новый штраф: "))
            if fine <= 0:
                print("Введите положительное число")
            break
        except ValueError:
            print("Введите целое положительное число")
    update_booktype_fine(token, book_id, fine)
    try:
        print("Штраф успешно изменен\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")


def show_all_books_by_booktype_in_table(token):
    show_all_booktypes(token)
    booktypes = get_all_booktypes(token)
    while True:
        print("Введите номер жанра из таблицы")
        try:
            num = int(input())
            if 0 <= num < len(booktypes):
                show_all_books_by_booktype(token, booktypes, num)
                break
            else:
                print("Некорректное число! Выберите число из указанных!\n")
        except ValueError:
            print("Некорректный символ! Выберите число из указанных!\n")

