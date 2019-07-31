# Описать класс «домашняя библиотека».
# Предусмотреть возможность работы с произвольным числом книг, поиска книги по какому-либо признаку
# (например, по автору или по году издания), добавления книг в библиотеку, удаления книг из нее,
# сортировки книг по разным полям.


class Library:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __eq__(self, other):
        if not isinstance(other, Library):
            return False
        if self.author != other.author:
            return False
        return True

    def __hash__(self):
        return self.author


book1 = Library('Онегин', 'Пушкин', 1999)
book2 = Library('Мцыри', 'Лермонтов', 1986)
book3 = Library('Война и мир', 'Толстой', 1995)


