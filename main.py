from library import *
from librarian import *
from books import *
from reader import *

library = Library()
print('Библиотека:')
print(library)
print()
librarian1 = Librarian('Марь Иванна')
librarian2 = Librarian('Евгения Барисовна')
librarian3 = Librarian('Евдакинья Георгевна')

print('Сотрудники:')
for i in (librarian1, librarian2, librarian3):
    print(i)
#roman = Roman()
#fantasy = Fantasy()
#educational = Educational()
print("\n\n")
while True:

    print("1. Добавить книгу в каталог")
    print("2. Найти книгу")
    print("3. Вернуть книгу")
    print("4. Вывести весь каталог")
    print("\n")

    print("Введите нужный пункт меню: ")
    check = input("")
    assert check.isdigit(), 'Нужно ввести цифру'
    check = int(check)

    if check == 1:
        print("Данную операцию может осуществить только библиотекарь.")
        code = input("Введите Ваш код сотрудника: ") #001, 002, 003
        if code == '001' or code == '002' or code == '003':
            print("Одобрено.")
            print("1. Фентези")
            print("2. Роман")
            print("3. Учебная литература")
            genre_num = int(input("Укажите жанр книги (0 - закончить): "))
            while genre_num != 0:
                if genre_num == 1:
                    fantasy.add_book()
                if genre_num == 2:
                    roman.add_book()
                if genre_num == 3:
                    educational.add_book()

                print("1. Фентези")
                print("2. Роман")
                print("3. Учебная литература")
                genre_num = int(input("Укажите жанр книги (0 - закончить): "))
        else:
            print("Неверный код. Операция отклонена.")
        print("\n\n")

    if check == 2:
        print("1. Фентези")
        print("2. Роман")
        print("3. Учебная литература")
        genre_num = int(input("Укажите интересующий жанр: "))
        if genre_num == 1:
            for key, value in fantasy.all_books().items():
                print(key, value)
            find_book(fantasy.all_books())
            print("Оставшиеся книги в данном жанре: ")
            for key, value in fantasy.all_books().items():
                print(key, value)

        if genre_num == 2:
            for key, value in roman.all_books().items():
                print(key, value)
            find_book(roman.all_books())
            print("Оставшиеся книги в данном жанре: ")
            for key, value in roman.all_books().items():
                print(key, value)
        if genre_num == 3:
            for key, value in educational.all_books().items():
                print(key, value)
            find_book(educational.all_books())
            print("Оставшиеся книги в данном жанре: ")
            for key, value in educational.all_books().items():
                print(key, value)
        print("\n\n")

    if check == 3:
        print("1. Фентези")
        print("2. Роман")
        print("3. Учебная литература")
        genre_num = int(input("Укажите жанр книги, которую хотите сдать: "))
        if genre_num == 1:
            for key, value in fantasy.all_books().items():
                print(key, value)
            back_book(fantasy.all_books())
            print("Оставшиеся книги в данном жанре: ")
            for key, value in fantasy.all_books().items():
                print(key, value)

        if genre_num == 2:
            for key, value in roman.all_books().items():
                print(key, value)
            back_book(roman.all_books())
            print("Оставшиеся книги в данном жанре: ")
            for key, value in roman.all_books().items():
                print(key, value)
        if genre_num == 3:
            for key, value in educational.all_books().items():
                print(key, value)
            back_book(educational.all_books())
            print("Оставшиеся книги в данном жанре: ")
            for key, value in educational.all_books().items():
                print(key, value)

        print("\n\n")

    if check == 4:
        print("Всего книг в библиотеке: ")
        print(library.count_of_books())
        print("Фентази: ", fantasy.all_books(), fantasy.count_books())
        print("Романы: ", roman.all_books(), roman.count_books())
        print("Учебная литература: ", educational.all_books(), educational.count_books())
        print("\n\n")
