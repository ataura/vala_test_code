import json
class LibraryDatabase:
    def __init__(self,filename):
        self.books = []
        self.filename = filename
        self.load_from_file(filename)
        try:
            with open(filename, "r") as file:
                books = [json.loads(line) for line in file]
        except FileNotFoundError:
            print("No existing database found. Starting with an empty list.")

    def add_book(self):
        book_name = input("Enter book name: ")
        author_name = input("Enter author name: ")
        year_published = input("Enter year published: ")
        isbn  = input("Enter ISBN: ")
        new_book = {
            "book_name": book_name,
            "author_name": author_name,
            "year_published": year_published,
            "isbn": isbn
        }
        print(f"New book added: {new_book['book_name']} by {new_book['author_name']} ({new_book['year_published']}) - ISBN: {new_book['isbn']}")
        do_you_want_to_save = input("Do you want to save this book to the database? (yes/no): ").strip().lower()
        if do_you_want_to_save == "yes":
          self.save_to_database(new_book)
        else:
          print("Book not saved to database.")
          print("Returning to main menu...\n\n")

    def save_to_database(self, new_book):
        self.books.append(new_book)
        self.books.sort(key=lambda x: x['year_published'])

        with open(self.filename, "w") as file:
            for book in self.books:
                file.write(json.dumps(book) + "\n")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                self.books = [json.loads(line) for line in file]
        except FileNotFoundError:
            print("No existing database found. Starting with an empty list.")

    def print_database(self):
        self.books.sort(key=lambda x: x['year_published'])
        print("Current database:")
        print(f"{'Book Name':<30}  {'Author Name':<20}  {'Year':<6}  {'ISBN':<15}")
        print("-" * 80)
        for book in self.books:
            print(f"{book['book_name']:<30}  {book['author_name']:<20}  {book['year_published']:<6}  {book['isbn']:<15}")
        print("-" * 80)
        print(f"Total number of books: {len(self.books)}\n\n")
