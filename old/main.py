from enum import Enum


class MarkupPage(Enum):
    # клетка, линейка, пустая
    squared = "клетка"
    ruled = "линейка"
    empty = "пустая"


class Orientation(Enum):
    # альбомная, книжная
    landskape = "альбомная"
    book = "книжная"


active = ["name", "do_numbering", "markup_page", "orientation",
          "number_of_page", "color_of_book", "publisher", "notes"]


class NoteBook:

    def __init__(self,
                 name,
                 do_numbering: bool,
                 markup_page: MarkupPage,
                 orientation: Orientation,
                 number_of_page, color_of_book, publisher,
                 notes: list):
        self.name = name
        self.do_numbering = do_numbering
        self.markup_page = markup_page
        self.orientation = orientation
        self.number_of_page = number_of_page
        self.color_of_book = color_of_book
        self.publisher = publisher
        self.notes = notes

    def get_info(self):
        for field in active:
            value = getattr(self, field) # == self.__getattr__(field)
            print(value)
        # for i in range(8):
        #     print(active[i])


    def Notes(self, number):
        self.number = number
        print(self.notes[number])

    @staticmethod
    def Info():
        print("Добрый день! \n Мы рады видеть вас в приложении записаная книжка")
        print("Вы можете создать новую записную книжку заполнив следующие пункты: ФИО, Нумерация стр(Да/Нет), "
              "Разметка страницы, Ориентация, количество страниц, цвет обложки, издательство, список записей")
        print("Спасибо, что выбрали нас!")


try1 = NoteBook("none", False, MarkupPage.empty, Orientation.book, 40, "red", "Alimp", ["Запись 1", "Pfgbcm 2", "and the third"])

print("Добрый день! \n Записная книжка открыта \n Заполним нашу записную книжку!")
"""
# ФИО
try1.name = input("введите ФИО: ")
# нумерация
ans = input("Включить нумерацию страниц (Да/Нет)?: ")
if ans == "Да":
    try1.do_numbering = True
else:
    try1.do_numbering = False
# Разметка страницы
ans = input("Разметка страницы - клетка, линейка, пустая: ")
if ans == "клетка":
    try1.markup_page = MarkupPage.squared
elif ans == "линейка":
    try1.markup_page = MarkupPage.ruled
else:
    try1.markup_page = MarkupPage.empty
# Ориентация
ans = input("Ориентация (альбомная, книжная): ")
if ans == "альбомная":
    try1.orientation = Orientation.landskape
else:
    try1.orientation = Orientation.book
# Кол-во страниц
try1.number_of_page = input("Введите количество страниц: ")
# Цвет обложки
try1.color_of_book = input("Цвет обложки: ")
# Издательство
try1.publisher = input("Издательство: ")
# Введите количество записей
units = int(input("Введите количество записей: "))
for i in range(units):
    recording = input("Введите запись")
    try1.notes.append(recording)

    def getParams(self, name, do_numbering, markup_page, orientation,
                 number_of_page, color_of_book, publisher, notes):
                 
    print(try1.name, try1.do_numbering, try1.markup_page, try1.orientation, try1.number_of_page, try1.color_of_book,
      try1.publisher, try1.notes)
"""
try1.get_info()
try1.Notes(1)
try1.Info()

# if __name__ == '__main__':
#     a = 1
