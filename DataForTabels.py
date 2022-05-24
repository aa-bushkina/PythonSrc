from endpoints.Book import *
from endpoints.BookType import *
from endpoints.Client import *
from endpoints.Entry import *
from endpoints.User import *


# def clean_tables():


def fill_tabels():
    username = "test_admin"
    password = "test_admin"
    token = log_in(username, password).token

    booktype1 = add_booktype(token=token, name="Роман", fine=100.0, day_count=30)['id']
    booktype2 = add_booktype(token=token, name="Психологическая", fine=560.0, day_count=20)['id']
    booktype3 = add_booktype(token=token, name="Ужасы", fine=230.0, day_count=60)['id']
    booktype4 = add_booktype(token=token, name="Детективы", fine=166.0, day_count=40)['id']
    booktype5 = add_booktype(token=token, name="Научные", fine=500.0, day_count=150)['id']
    booktype6 = add_booktype(token=token, name="Приключения", fine=270.0, day_count=60)['id']
    booktype7 = add_booktype(token=token, name="Учебная", fine=150.0, day_count=200)['id']
    booktype8 = add_booktype(token=token, name="Фантастика", fine=330.0, day_count=38)['id']

    book1 = add_book(token=token, name="Властелин колец",
                     cnt=8, booktype_id=booktype1)['id']
    book2 = add_book(token=token, name="Гордость и предубеждение",
                     cnt=12, booktype_id=booktype1)['id']
    book3 = add_book(token=token, name="Темные начала",
                     cnt=6, booktype_id=booktype1)['id']
    book4 = add_book(token=token, name="Ребекка",
                     cnt=4, booktype_id=booktype1)['id']
    book5 = add_book(token=token, name="Унесенные ветром",
                     cnt=20, booktype_id=booktype1)['id']
    book6 = add_book(token=token, name="Дюна",
                     cnt=15, booktype_id=booktype1)['id']

    book7 = add_book(token=token, name="Социальная психология",
                     cnt=11, booktype_id=booktype2)['id']
    book8 = add_book(token=token, name="Сказать жизни “Да!”",
                     cnt=6, booktype_id=booktype2)['id']
    book9 = add_book(token=token, name="Мой голос останется с Вами",
                     cnt=7, booktype_id=booktype2)['id']
    book10 = add_book(token=token, name="Хочу и буду", cnt=6,
                      booktype_id=booktype2)['id']
    book11 = add_book(token=token, name="7 навыков высокоэффективных людей",
                      cnt=12, booktype_id=booktype2)['id']
    book12 = add_book(token=token, name="Миллионер с хорошей кармой",
                      cnt=11, booktype_id=booktype2)['id']
    book13 = add_book(token=token, name="Судьба шлёт знаки или на*ер",
                      cnt=10, booktype_id=booktype2)['id']
    book14 = add_book(token=token, name="Психология убеждения",
                      cnt=28, booktype_id=booktype2)['id']
    book15 = add_book(token=token, name="Игры, в которые играют люди",
                      cnt=2, booktype_id=booktype2)['id']
    book16 = add_book(token=token, name="Поток. Психология оптимального переживания",
                      cnt=1, booktype_id=booktype2)['id']
    book17 = add_book(token=token, name="Эмоциональный интеллект", cnt=3, booktype_id=booktype2)['id']

    book18 = add_book(token=token, name="Мизеры",
                      cnt=18, booktype_id=booktype3)['id']
    book19 = add_book(token=token, name="Сияние",
                      cnt=3, booktype_id=booktype3)['id']
    book20 = add_book(token=token, name="Дракула",
                      cnt=1, booktype_id=booktype3)['id']
    book21 = add_book(token=token, name="Оно",
                      cnt=12, booktype_id=booktype3)['id']
    book22 = add_book(token=token, name="Кэрри",
                      cnt=3, booktype_id=booktype3)['id']

    boo23 = add_book(token=token, name="Шерлок Холмс",
                     cnt=38, booktype_id=booktype4)['id']
    book24 = add_book(token=token, name="Убийство в восточном экспрессе",
                      cnt=5, booktype_id=booktype4)['id']
    book25 = add_book(token=token, name="Дочь времни",
                      cnt=14, booktype_id=booktype4)['id']
    book26 = add_book(token=token, name="39 ступеней",
                      cnt=3, booktype_id=booktype4)['id']
    book27 = add_book(token=token, name="Молчание ягнят",
                      cnt=8, booktype_id=booktype4)['id']
    book28 = add_book(token=token, name="Крестный отец",
                      cnt=23, booktype_id=booktype4)['id']
    book29 = add_book(token=token, name="Вечный сон",
                      cnt=10, booktype_id=booktype4)['id']
    book30 = add_book(token=token, name="Лунный камень",
                      cnt=1, booktype_id=booktype4)['id']

    book31 = add_book(token=token, name="Анатомия преступления",
                      cnt=34, booktype_id=booktype5)['id']
    book32 = add_book(token=token, name="Книга всеобщих заблуждений",
                      cnt=24, booktype_id=booktype5)['id']
    book33 = add_book(token=token, name="Паразиты. Тайный мир",
                      cnt=40, booktype_id=booktype5)['id']
    book34 = add_book(token=token, name="Агрессия или так называемое зло",
                      cnt=2, booktype_id=booktype5)['id']
    book35 = add_book(token=token, name="Калибан и Ведьма",
                      cnt=5, booktype_id=booktype5)['id']
    book36 = add_book(token=token, name="Зачем мы спим",
                      cnt=11, booktype_id=booktype5)['id']
    book37 = add_book(token=token, name="Мозг и душа",
                      cnt=16, booktype_id=booktype5)['id']
    book38 = add_book(token=token, name="Пандемия: Всемирная история смертельных вирусов",
                      cnt=20, booktype_id=booktype4)['id']

    book39 = add_book(token=token, name="Два капитана",
                      cnt=8, booktype_id=booktype6)['id']
    book40 = add_book(token=token, name="Часодеи",
                      cnt=22, booktype_id=booktype6)['id']
    book41 = add_book(token=token, name="Белый клык",
                      cnt=4, booktype_id=booktype6)['id']
    book42 = add_book(token=token, name="Вокруг света за 80 дней",
                      cnt=21, booktype_id=booktype6)['id']

    book43 = add_book(token=token, name="Контурные карты 7 класс",
                      cnt=9, booktype_id=booktype7)['id']
    book44 = add_book(token=token, name="Математика 5 класс",
                      cnt=13, booktype_id=booktype7)['id']
    book45 = add_book(token=token, name="Обществознание 8 класс",
                      cnt=19, booktype_id=booktype7)['id']
    book46 = add_book(token=token, name="История 11 класс",
                      cnt=22, booktype_id=booktype7)['id']
    book47 = add_book(token=token, name="Русский язык 9 класс",
                      cnt=6, booktype_id=booktype7)['id']
    book48 = add_book(token=token, name="Литература 9 класс",
                      cnt=18, booktype_id=booktype7)['id']
    book49 = add_book(token=token, name="Сборник задач ЕГЭ 2022",
                      cnt=4, booktype_id=booktype7)['id']

    book50 = add_book(token=token, name="Путешествия Гулливера",
                      cnt=4, booktype_id=booktype8)['id']
    book51 = add_book(token=token, name="Парк Юрского периода",
                      cnt=9, booktype_id=booktype8)['id']
    book52 = add_book(token=token, name="2001: Космическая Одиссея",
                      cnt=11, booktype_id=booktype8)['id']
    book53 = add_book(token=token, name="Нейромант",
                      cnt=30, booktype_id=booktype8)['id']
    book54 = add_book(token=token, name="Мечтают ли андроиды об электроовцах?",
                      cnt=5, booktype_id=booktype8)['id']
    book55 = add_book(token=token, name="Я, робот",
                      cnt=24, booktype_id=booktype8)['id']
    book56 = add_book(token=token, name="День триффидов",
                      cnt=4, booktype_id=booktype8)['id']
    book57 = add_book(token=token, name="Янки из Коннектикута при дворе короля Артура",
                      cnt=5, booktype_id=booktype8)['id']
    book58 = add_book(token=token, name="Алиса в стране чудес",
                      cnt=8, booktype_id=booktype8)['id']
    book59 = add_book(token=token, name="Война миров",
                      cnt=5, booktype_id=booktype8)['id']
    book60 = add_book(token=token, name="Звездный десант",
                      cnt=15, booktype_id=booktype8)['id']
    book61 = add_book(token=token, name="Странная история доктора Джекила и мистера Хайда",
                      cnt=18, booktype_id=booktype8)['id']
    book62 = add_book(token=token, name="Двадцать тысяч лье под водой",
                      cnt=12, booktype_id=booktype8)['id']

    client1 = add_client(token=token, firstname="Александра", lastname="Авилова", pathername="Сергеевна",
                         pass_ser="1234", pass_num="452889")['id']
    client2 = add_client(token=token, firstname="Ксения", lastname="Никишова", pathername="Сергеевна",
                         pass_ser="1564", pass_num="454789")['id']
    client3 = add_client(token=token, firstname="Елена", lastname="Ярцева", pathername="Андреевна",
                         pass_ser="2834", pass_num="456789")['id']
    client4 = add_client(token=token, firstname="Родион", lastname="Болдырев", pathername="Романович",
                         pass_ser="6834", pass_num="406789")['id']
    client5 = add_client(token=token, firstname="Андрей", lastname="Давыдов", pathername="Ильич",
                         pass_ser="2234", pass_num="452289")['id']

    entry1 = add_entry(token, client1, book1)
    entry1 = add_entry(token, client2, book2)
    entry1 = add_entry(token, client2, book3)
    entry1 = add_entry(token, client2, book4)
    entry1 = add_entry(token, client3, book5)
    entry1 = add_entry(token, client3, book6)
    entry1 = add_entry(token, client4, book7)
    entry1 = add_entry(token, client5, book8)
