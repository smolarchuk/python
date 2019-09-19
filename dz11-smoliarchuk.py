# Описать класс «домашняя библиотека».
# Предусмотреть возможность работы с произвольным числом книг, поиска книги по какому-либо признаку
# (например, по автору или по году издания), добавления книг в библиотеку, удаления книг из нее,
# сортировки книг по разным полям.


class Library:
    books = []

    def __init__(self, author, title, year):
        """Инициализация атрибутов книги"""
        Library.books.append(self.__dict__)
        self.author = str(author)
        self.title = str(title)
        self.year = str(year)

    # def book_description(self):
    #     """Вывод книги в человеческом формате"""
    #     description = f"{self.author}, {self.title}, {self.year}"
    #     return description.title()

    @staticmethod
    def search_books():
        """Поиск книги в библиотеке"""
        phrase = {str(input("Введите запрос: "))}
        search_result = list(filter(lambda x: {k: v for k, v in x.items() if v in phrase}, Library.books))
        if len(search_result) > 0:
            print("Результаты поиска:")
            for x in search_result:
                print(x)
        else:
            print('Нет такой книги в библиотеке')

    @classmethod
    def add_book(cls):
        return cls(
            str(input('Автор: ')),
            str(input('Название: ')),
            str(input('Год: ')),
        )

    def delete_book(self):
        pass

    @staticmethod
    def sort_books():
        phrase = str(input("Введите запрос: "))
        sorted_library = sorted(Library.books, key=lambda x: x[phrase])
        for x in sorted_library:
            print(x)

    @staticmethod
    def show_library():
        for x in Library.books:
            print(x)


book1 = Library('Онегин', 'Пушкин', 1999)
book2 = Library('Мцыри', 'Лермонтов', 1986)
book3 = Library('Война и мир', 'Толстой', 1995)

book1.show_library()
