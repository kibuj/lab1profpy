class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, book_info):
        if book_id not in self.books:
            self.books[book_id] = book_info

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]

    def search_book(self, book_id):
        if book_id in self.books:
            print(self.books[book_id])

    def display_books(self):
        for book_id, info in self.books.items():
            print(f"\nНомер книги: {book_id}")
            print(f"  Автор: {info['author']}")
            print(f"  Назва: {info['title']}")
            print(f"  Видавництво: {info['publisher']}")
            print(f"  Жанр: {info['genre']}")
            print(f"  Рік видання: {info['year']}")


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
        if choice == "2":
            book_id = (int(input("Яку книгу видалити(id)")))
            library.remove_book(book_id)
        if choice == "3":
            book_id = (int(input("Вкажіть id книги")))
            library.search_book(book_id)
        if choice == "4":
            library.display_books()
        if choice == "5":
            break
main()
