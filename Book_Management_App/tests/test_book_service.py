import pytest
import os
from services.book_service import BookService
from repository.book_repository import BookRepository
from domain.book import Book

TEST_FILE = "tests/test_books.json"


@pytest.fixture
def book_service():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

    repo = BookRepository(TEST_FILE)
    return BookService(repo)


def test_add_book(book_service):
    """
    - Verifies that a book can be added successfully
    """
    book_service.add_book(Book("Test Book", "Author"))
    books = book_service.get_books()

    assert len(books) == 1
    assert books[0].title == "Test Book"


def test_list_books(book_service):
    """
    - Verifies that multiple books can be listed
    - Ensures repository returns all stored books
    """
    book_service.add_book(Book("Book 1", "Author 1"))
    book_service.add_book(Book("Book 2", "Author 2"))

    assert len(book_service.get_books()) == 2


def test_checkout_book(book_service):
    """
    - Verifies successful checkout of an available book
    - Confirms availability status changes to False
    """
    book_service.add_book(Book("Checkout Book", "Author"))

    book = book_service.get_books()[0]
    checked_out = book_service.checkout_book(book.book_id, "test@email.com")

    assert checked_out.available is False


def test_checkout_unavailable_book(book_service):
    """
    - Prevents checkout of a book that is already checked out
    - Ensures business rule enforcement
    """
    book_service.add_book(Book("Already Out", "Author"))

    book = book_service.get_books()[0]
    book_service.checkout_book(book.book_id, "a@test.com")

    with pytest.raises(Exception):
        book_service.checkout_book(book.book_id, "b@test.com")


def test_checkin_book(book_service):
    """
    - Verifies successful check-in of a checked-out book
    - Confirms availability status changes back to True
    """
    book_service.add_book(Book("Return Book", "Author"))

    book = book_service.get_books()[0]
    book_service.checkout_book(book.book_id, "a@test.com")

    checked_in = book_service.checkin_book(book.book_id)

    assert checked_in.available is True


def test_checkin_available_book(book_service):
    """
    - Allows check-in of an already available book
    - Ensures system handles redundant operations gracefully
    """
    book_service.add_book(Book("Available Book", "Author"))

    book = book_service.get_books()[0]
    checked_in = book_service.checkin_book(book.book_id)

    assert checked_in.available is True


def test_delete_book(book_service):
    """
    - Verifies deletion of an existing book
    - Ensures book is removed from storage
    """
    book_service.add_book(Book("Delete Me", "Author"))

    book_id = book_service.get_books()[0].book_id
    book_service.delete_book(book_id)

    assert len(book_service.get_books()) == 0


def test_delete_nonexistent_book(book_service):
    """
    - Attempts to delete a non-existent book
    - Confirms system does not crash and handles the case safely
    """
    book_service.delete_book("non-existent-id")
