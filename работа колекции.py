from collections import namedtuple
from collections import Counter

class Biblioteka():
    def __init__(self, chapter, book_in, newspapers_in, journal_in):
        self.chapter = chapter
        self.book_in = book_in
        self.newspapers_in = newspapers_in
        self.journal_in = journal_in

        
class books_by_author(): #класс с данными про книги автора(сколько их и сколько в библиотеке)
    def __init__(self, author, book_in, book_in_bib):
        self.author = author
        self.book_in = book_in
        self.book_in_bib = book_in_bib


class reader(): #читатель (имя фамилия номер билета)
    def __init__(self, first_name, last_name, card_number):
        self.first_name = first_name
        self.last_name = last_name
        self.card_number = card_number


class readers_ticket (reader): #читательский билет (имя, фамилия, количество книг дома, количествол сданых книг)
    def __init__(self, first_name, last_name, book_in_home, book_in_bib):
        super(readers_ticket, self).__init__(first_name, last_name)
        self.book_in_home = book_in_home
        self.book_in_bib = book_in_bib


#коллекции в питоне, namedtupl
author = namedtuple('author', 'name age books')
hum = author(name="Vera", age=18, books=0)
print("имя автора: "  + hum[0])
print("данные автора" + str(hum))

#коллекции в питоне, counter
author_fan = (
 ('Pushkin', 'Tolstoy'),
 ('Fet', 'Dostoevsky'),
 ('Tolstoy', 'Fleuruk'),
 ('Kanskiyts', 'Pushkin'),
 ('Tyutchev', 'Fleuruk'),
 ('Tolstoy', 'Dostoevsky'),)
favs = Counter(name for name, author_fan in author_fan)
print("любимые писатели: " + str(favs))


