from books import *

class Library:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            raise Exception("У данного класса может быть только один экземпляр")

    def __init__(self, lib_name = 'Библиотека им. Маяковского'):
        self.lib_name = lib_name
        self.books = 0

    def __str__(self):
        return f' {self.lib_name}\n общее количество книг: {self.books}'

    def count_of_books(self):
        count = educational.count_books() + roman.count_books() + fantasy.count_books()
        return count
