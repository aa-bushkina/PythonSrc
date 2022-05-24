from Details import *


def add_client_in_table(token):
    print("Введите данные нового клиента")
    print("Имя: ")
    firstname = enter_word()
    print("Фамилия: ")
    lastname = enter_word()
    print("Отчество: ")
    pathername = enter_word()
    while True:
        try:
            pass_ser = input("Введите серию паспорта: ")
            if pass_ser.isdigit() and len(pass_ser) == 4:
                break
            print("Введите строку из 4 цифр\n")
        except ValueError:
            print("Введите строку из 4 цифр\n")
    while True:
        try:
            pass_num = input("Введите номер паспорта: ")
            if pass_num.isdigit() and len(pass_num) == 6:
                break
            print("Введите строку из 6 цифр")
        except ValueError:
            print("Введите строку из 6 цифр")
    try:
        add_client(token, lastname, firstname, pathername, pass_ser, pass_num)
        print("Клиент успешно добавлен\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")


def delete_client_from_table(token):
    while True:
        show_all_clients(token)
        print("Выберите номер клиента: ")
        try:
            client_num = int(input())
            if 0 <= client_num < len(get_all_clients(token)):
                client = get_all_clients(token)[client_num]
                break
            else:
                print("Некорректное число! Выберите число из указанных!\n")
        except ValueError:
            print("Некорректный символ! Выберите номер из указанных!\n")
    try:
        delete_client(token, client['id'])
        print("Клиент успешно удален\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")




def update_client_firstname_in_table(token):
    while True:
        show_all_clients(token)
        print("Выберите номер клиента")
        try:
            client_num = int(input())
            if 0 <= client_num < len(get_all_clients(token)):
                client_id = get_all_clients(token)[client_num]['id']
                break
        except ValueError:
            print("Некорректный символ! Выберите номер из указанных!\n")
    while True:
        try:
            firstname = input("Введите новое имя: ")
            if not (firstname.isalpha() or len(firstname) <= 20):
                print("Введите строку из букв длиной меньше 20 символов\n")
            break
        except ValueError:
            print("Введите строку из букв длиной меньше 20 символов\n")
    update_client_firstname(token, client_id, firstname)
    try:
        print("Имя клиента успешно изменено\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")


def update_client_lastname_in_table(token):
    while True:
        show_all_clients(token)
        print("Выберите номер клиента")
        try:
            client_num = int(input())
            if 0 <= client_num < len(get_all_clients(token)):
                client_id = get_all_clients(token)[client_num]['id']
                break
        except ValueError:
            print("Некорректный символ! Выберите номер из указанных!\n")
    while True:
        try:
            lastname = input("Введите новую фамилию: ")
            if not (lastname.isalpha() or len(lastname) <= 20):
                print("Введите строку из букв длиной меньше 20 символов\n")
            break
        except ValueError:
            print("Введите строку из букв длиной меньше 20 символов\n")
    update_client_lastname(token, client_id, lastname)
    try:
        print("Фамилия клиента успешно изменена\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")


def update_client_passport_in_table(token):
    while True:
        show_all_clients(token)
        print("Выберите номер клиента")
        try:
            client_num = int(input())
            if 0 <= client_num < len(get_all_clients(token)):
                client_id = get_all_clients(token)[client_num]['id']
                break
        except ValueError:
            print("Некорректный символ! Выберите номер из указанных!\n")
    while True:
        try:
            pass_ser = input("Введите новую серию паспорта: ")
            if pass_ser.isdigit() and len(pass_ser) == 4:
                break
            print("Введите строку из 4 цифр\n")
        except ValueError:
            print("Введите строку из 4 цифр\n")
    while True:
        try:
            pass_num = input("Введите новый номер паспорта: ")
            if pass_num.isdigit() and len(pass_num) == 6:
                break
            print("Введите строку из 6 цифр\n")
        except ValueError:
            print("Введите строку из 6 цифр\n")
    update_client_passport(token, client_id, pass_ser, pass_num)
    try:
        print("Имя клиента успешно изменено\n")
    except Exception as e:
        print(str(e)[str(e).find("Ошибка"):len(str(e)) - 2] + "\n")
