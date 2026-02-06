
from repository.book_repository import BookRepository
from domain.book import Book
from typing import List

class BookService:
    def __init__(self, repo):
        self.repo = repo

    def add_book(self, book):
        self.repo.add(book)
        return book

    def get_books(self):
        return self.repo.list_all()

    def update_book(self, book: Book):
        self.repo.update(book)

    def delete_book(self, book_id):
        book = self.repo.get_by_id(book_id)
        if book is None:
            print("Book not found")
            return False

        self.repo.delete(book_id)
        return True

    def checkout_book(self, book_id: str, user_email: str):
        books = self.get_books()
        for b in books:
            if b.book_id == book_id:
                b.checkout(user_email)
                self.update_book(b)
                return b
        raise Exception("Book not found")

    def checkin_book(self, book_id: str):
        books = self.get_books()
        for b in books:
            if b.book_id == book_id:
                b.checkin()
                self.update_book(b)
                return b
        raise Exception("Book not found")
