import json
from pathlib import Path
from typing import List
from domain.book import Book

class BookRepository:
    def __init__(self, filepath: str = None):
        # Always point to the correct books.json in the repo
        if filepath:
            self.filepath = Path(filepath)
        else:
            # __file__ is the current script (book_repository.py)
            repo_root = Path(__file__).resolve().parent.parent  # project root
            self.filepath = repo_root / "data" / "books.json"

        # Make sure folder exists
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

        # Create file if missing
        if not self.filepath.exists():
            with open(self.filepath, "w") as f:
                f.write("[]")  # empty JSON list

    def _read_file(self) -> List[dict]:
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _write_file(self, books: List[dict]):
        with open(self.filepath, "w") as f:
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

    def delete(self, book_id: str):
        books = self._read_file()
        books = [b for b in books if b["book_id"] != book_id]
        self._write_file(books)
