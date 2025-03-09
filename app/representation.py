from abc import ABC, abstractmethod

from app.book import Book


class Representation(ABC):
    @abstractmethod
    def display(self, book: Book):
        pass

    @abstractmethod
    def print_book(self, book: Book):
        pass


class ConsoleRepresentation(Representation):
    def display(self, book: Book):
        print(book.content)

    def print_book(self, book: Book):
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseRepresentation(Representation):
    def display(self, book: Book):
        print(book.content[::-1])

    def print_book(self, book: Book):
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
