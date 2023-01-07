from books import *

class Reader:
    def __init__(self, book, amount, dict):
        self.book = book
        self.amount = amount
        self.books_dict = dict

    def take_book(self):
        if self.book in self.books_dict:
            self.books_dict[self.book] -= self.amount
        else:
            print("\nТакой книги нет.\n")

    def give_book(self):
        if self.book in self.books_dict:
            self.books_dict[self.book] += self.amount
        else:
            self.books_dict[self.book] = self.amount

def find_book(dict):
    name_book = input("Выберите книгу: ")
    amount_book = int(input("Количество: "))
    reader = Reader(name_book, amount_book, dict)
    reader.take_book()

def back_book(dict):
    name_book = input("Введите название книги: ")
    amount_book = int(input("Количество: "))
    reader = Reader(name_book, amount_book, dict)
    reader.give_book()