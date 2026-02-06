from repository.book_repository import BookRepository
from domain.book import Book
from typing import List

class BookService:
    def __init__(self, repo: BookRepository):
        self.repo = repo

    def add_book(self, book: Book):
        self.repo.create(book)

    def get_books(self) -> List[Book]:
        return self.repo.list_all()

    def update_book(self, book: Book):
        self.repo.update(book)

    def delete_book(self, book_id):
        books = self.repo.get_by_id(book_id)
        if not books:
            raise ValueError("Book not found.")
        self.repo.delete(book_id)

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
