import json
import os
from pathlib import Path
from typing import List
from domain.book import Book

class BookRepository:
    def __init__(self, file_path="data/books.json"):
        self.file_path = file_path

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def _load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)
        
    def add(self, book):
        books = self._load()
        books.append(book.to_dict())
        self._save(books)

    def _save(self, books):
        with open(self.file_path, "w") as f:
            json.dump(books, f, indent=4)
            
    def _read_file(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _write_file(self, books: List[dict]):
        with open(self.file_path, "w") as f:
            json.dump(books, f, indent=2)

    def create(self, book: Book):
        books = self._read_file()
        books.append(book.__dict__)
        self._write_file(books)

    def list_all(self) -> List[Book]:
        return [Book(**b) for b in self._read_file()]

    def update(self, book: Book):
        books = self._read_file()
        for idx, b in enumerate(books):
            if b["book_id"] == book.book_id:
                books[idx] = book.__dict__
                break
        self._write_file(books)

    def delete(self, book_id):
        books = self._load()
        books = [b for b in books if b["book_id"] != book_id]
        self._save(books)
        
    
    def get_by_id(self, book_id):
        books = self._load()
        for book in books:
            if book["book_id"] == book_id:
                return book
        return None
    
    # def get_all(self):
    #     return self._load()
