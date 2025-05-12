import sqlite3

class Library:
    def __init__(self):
        self.books = {}
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                author TEXT,
                title TEXT,
                publisher TEXT,
                genre TEXT,
                year Text
            )
        """)
        self.conn.commit()

    def add_book(self, book_id, book_info):
        if book_id not in self.books:
            self.books[book_id] = book_info
        self.cursor.execute("""
            INSERT OR REPLACE INTO books (id, author, title, publisher, genre, year)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (book_id, book_info['author'], book_info['title'], book_info['publisher'], book_info['genre'], book_info['year']))
        self.conn.commit()


    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
        self.cursor.execute("""
            DELETE FROM books WHERE id = ?
        """, (book_id,))
        self.conn.commit()

    def search_book(self, book_id):
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = self.cursor.fetchone()
        if book_id in self.books:
            print(self.books[book_id])

    def display_books(self):
        self.cursor.execute("SELECT * FROM books")
        all_books = self.cursor.fetchall()
        for book in all_books:
            print(f"\nНомер книги: {book[0]}")
            print(f"  Автор: {book[1]}")
            print(f"  Назва: {book[2]}")
            print(f"  Видавництво: {book[3]}")
            print(f"  Жанр: {book[4]}")
            print(f"  Рік видання: {book[5]}")

    def __del__(self):
        self.conn.close()


def main():
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Додати книгу")
        print("2. Видалити книгу")
        print("3. Переглянути книгу за номером")
        print("4. Вивести всі книги")
        print("5. Вийти")

        choice = input("\n")

        if choice == "1":
            book_id = int(input('Номер книги:\n'))
            book_info = {
                "author": input("Автор: "),
                "title": input("Назва: "),
                "publisher": input("Видавництво: "),
                "genre": input("Жанр: "),
                "year": input("Рік видання: ")
            }
            library.add_book(book_id, book_info)
        elif choice == "2":
            book_id = int(input("Яку книгу видалити(id): "))
            library.remove_book(book_id)
        elif choice == "3":
            book_id = int(input("Вкажіть id книги: "))
            library.search_book(book_id)
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            break
        else:
            print("Невірний вибір. Спробуйте ще.")

main()