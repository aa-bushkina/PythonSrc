from AdminApp.AdminMenu import *
from UserApp.UserMenu import *
from DataForTabels import *


def print_header():
    for number in range(110):
        print("_", end='')
    print("\n")
    for number in range(50):
        print(" ", end='')
    print("БИБЛИОТЕКА", end='')
    for number in range(50):
        print(" ", end='')
    print("\n")
    for number in range(108):
        print("_", end='')
    print("\n")


def log_in_sys():
    print("Введите логин: ")
    username = input()
    print("Введите пароль: ")
    password = input()
    user_info = log_in(username, password)
    return user_info


def main():
    fill_tabels()
    print_header()
    while True:
        print("1 - Войти как пользователь")
        print("2 - Войти как администратор")
        print("0 - Завершить")
        action = input()
        match action:
            case "1":
                try:
                    user_info = log_in_sys()
                    token = user_info.token
                    client_id = user_info.client_id
                    user_app(token, client_id)
                except Exception:
                    print("Ошибка авторизации\n")
            case "2":
                try:
                    user_info = log_in_sys()
                    token = user_info.token
                    if user_info.is_admin:
                        admin_app(token)
                    else:
                        print("Доступ запрещен\n")
                except Exception:
                    print("Ошибка авторизации\n")
            case "0":
                break
            case _:
                print("Некорректное действие! Выберите действие из указанных!\n")


if __name__ == '__main__':
    main()
