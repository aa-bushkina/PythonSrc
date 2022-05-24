from Details import *


def add_book_in_table(token):
    is_ok_action = False
    while not is_ok_action:
        print("1 - Добавить экземпляр существующей книги")
        print("2 - Добавить новую книгу")
        print("3 - Посмотреть список книг")
        print("0 - Вернуться назад")
        action = input()
        match action:
            case "1":
                change_book_cnt(token, False)
            case "2":
                print("Введите данные новой книги")

                name = input("Название: ")
                print("Введите количество книг: ")
                cnt = enter_quantity()
                while True:
                    print("Выберите номер жанра: ")
                    show_all_booktypes(token)
                    booktype_num = int(input())
                    if 0 <= booktype_num < len(get_all_booktypes(token)):
                        booktype = get_all_booktypes(token)[booktype_num]
                        add_book(token, name, cnt, booktype['id'])
                        print("Книга успешно добавлена\n")
                        break
                    else:
                        print("Некорректное число! Выберите число из указанных!")
            case "3":
                show_all_books(token)
            case "0":
                break
            case _:
                print("Некорректное действие! Выберите действие из указанных!")


def delete_book_from_table(token):
    try:
        change_book_cnt(token, True)
        print("Книги успешно удалены\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")


def change_book_cnt(token, is_delete):
    while True:
        show_all_books(token)
        print("Выберите номер книги")
        book_num = int(input())
        if 0 <= book_num < len(get_all_books(token)):
            book_id = get_all_books(token)[book_num]['id']
            break
    while True:
        print("Введите количество книг: ")
        num_of_books = enter_quantity()
        if is_delete:
            if num_of_books > get_book(token, book_id)['cnt']:
                print("Книг меньше, чем вы хотите удалить!")
            else:
                update_book_cnt(token, book_id, get_book(token, book_id)['cnt'] - num_of_books)
                break
        else:
            update_book_cnt(token, book_id, get_book(token, book_id)['cnt'] + num_of_books)
            break
