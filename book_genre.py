from books import *


class Genre_book(ABC):
    def __init__(self):
        self.product = HotDog()

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def title(self):
        pass

    @abstractmethod
    def topping(self):
        pass

    def get_product(self):
        return self.product

class Book_genre1(Genre_book):
    def title(self):
        print('Жанр Фентази')

    def reset(self):
        self.fgenre = Fantasy()

    def genre_add(self):
        self.fgenre.add_book()

    def genre_list(self):
        self.fgenre.all_books()


class Book_genre2(Genre_book):
    def title(self):
        print('Жанр Роман')

    def reset(self):
        self.rgenre = Roman()

    def genre_add(self):
        self.rgenre.add_book()

    def genre_list(self):
        self.rgenre.all_books()

class Book_genre3(Genre_book):
    def title(self):
        print('Жанр Учебная литература')

    def reset(self):
        self.egenre = Educational()

    def genre_add(self):
        self.egenre.add_book()

    def genre_list(self):
        self.egenre.all_books()

roman = Book_genre2()
fantasy = Book_genre1()
educational = Book_genre3()

