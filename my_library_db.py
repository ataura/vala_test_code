import sys
import json
from lib import LibraryDatabase

def main():
  
    while True:
        print("Select operation:")
        print("1. Add new book")
        print("2. Print current database")
        print("Q|q exit the program")
        choice = input("Enter choice(1/2/Q|q): ").strip().lower()
        if choice in ("1", "2", "q"):
            if choice == "1":
                LibraryDatabase.add_book()
            elif choice == "2":
               LibraryDatabase.print_database()
            elif choice == "q":
                print("Exiting")
                break
            else:
                print("Invalid input")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python my_library_db.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    LibraryDatabase = LibraryDatabase.LibraryDatabase(filename)
    LibraryDatabase.print_database()
    main()