from abc import ABC, abstractmethod

class Books(ABC):
    def __init__(self):
        self.books_dict = dict()

    @abstractmethod
    def type_book(self):
        pass

    def add_book(self):
        new_book = input('Введите название книги: ').strip().title()
        book_amount = input('Сколько копий? \n').strip()
        assert book_amount.isdigit(), 'Нужно ввести число'
        book_amount = int(book_amount)

        if new_book not in self.books_dict:
            self.books_dict[new_book] = book_amount
        else:
            self.books_dict[new_book] += book_amount

    def all_books(self):
        return self.books_dict

    def count_books(self):
        return sum(self.books_dict.values())

    def __getitem__(self, item):
        return self.books_dict[item]

    def __str__(self):
        return ''.join(f'Название книги: {key}, Количество: {value} \n' for key, value in self.books_dict.items() )


class Fantasy(Books):
    def type_book(self):
        return "Фэнтези"

class Roman(Books):
    def type_book(self):
        return "Романы"

class Educational(Books):
    def type_book(self):
        return "Учебная литература"

roman = Roman()
fantasy = Fantasy()
educational = Educational()
