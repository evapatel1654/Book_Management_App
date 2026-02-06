from services.book_service import BookService
from repository.book_repository import BookRepository
from domain.book import Book

# Use the repository with fixed path
repo = BookRepository()
service = BookService(repo)

def main():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Checkout Book\n4. Checkin Book\n5. Delete Book\n0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre (optional): ") or None
            year = input("Publication Year (optional): ")
            year = int(year) if year else None
            page_count = input("Page Count (optional): ")
            page_count = int(page_count) if page_count else None
            rating = input("Average Rating (optional): ")
            rating = float(rating) if rating else None
            ratings_count = input("Ratings Count (optional): ")
            ratings_count = int(ratings_count) if ratings_count else None
            price = input("Price USD (optional): ")
            price = float(price) if price else None
            publisher = input("Publisher (optional): ") or None
            language = input("Language (optional): ") or None
            fmt = input("Format (optional): ") or None

            book = Book(
                title=title,
                author=author,
                genre=genre,
                publication_year=year,
                page_count=page_count,
                average_rating=rating,
                ratings_count=ratings_count,
                price_usd=price,
                publisher=publisher,
                language=language,
                format=fmt
            )
            service.add_book(book)
            print(f"Book added: {book.title}")

        elif choice == "2":
            books = service.get_books()
            if not books:
                print("No books available.")
            else:
                for b in books:
                    print(f"{b.book_id} | {b.title} | Author: {b.author} | Available: {b.available}")

        elif choice == "3":
            book_id = input("Book ID to checkout: ")
            email = input("User email: ")
            try:
                b = service.checkout_book(book_id, email)
                print(f"Checked out: {b.title}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            book_id = input("Book ID to checkin: ")
            try:
                b = service.checkin_book(book_id)
                print(f"Checked in: {b.title}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            book_id = input("Book ID to delete: ")
            try:
                service.delete_book(book_id)
                print(f"Deleted book ID: {book_id}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
