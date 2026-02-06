from typing import Optional
from datetime import datetime
import uuid

class Book:
    def __init__(
        self,
        title: str,
        author: str,
        genre: Optional[str] = None,
        publication_year: Optional[int] = None,
        page_count: Optional[int] = None,
        average_rating: Optional[float] = None,
        ratings_count: Optional[int] = None,
        price_usd: Optional[float] = None,
        publisher: Optional[str] = None,
        language: Optional[str] = None,
        book_format: Optional[str] = None,
        in_print: Optional[bool] = True,
        sales_millions: Optional[float] = None,
        last_checkout: Optional[str] = None,
        available: Optional[bool] = True,
        book_id: Optional[str] = None,
    ):
        self.book_id = book_id or str(uuid.uuid4())
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.page_count = page_count
        self.average_rating = average_rating
        self.ratings_count = ratings_count
        self.price_usd = price_usd
        self.publisher = publisher
        self.language = language
        self.in_print = in_print
        self.sales_millions = sales_millions
        self.last_checkout = last_checkout
        self.book_format = book_format
        self.available = available

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "publication_year": self.publication_year,
            "page_count": self.page_count,
            "average_rating": self.average_rating,
            "ratings_count": self.ratings_count,
            "price_usd": self.price_usd,
            "publisher": self.publisher,
            "language": self.language,
            "book_format": self.book_format,
            "available": self.available
        }
    def checkout(self, user_email: str):
        if not self.available:
            raise Exception("Book already checked out.")
        self.available = False
        self.last_checkout = datetime.now().isoformat()

    def checkin(self):
        self.available = True
        self.last_checkout = None
