'''
Implement a Python program that collects book information. The program starts with three options: 
entering new book, searching a book, exit.

* Entering new book: The program will ask to enter: book title, book author, publisher, publication date.
  Input will be (comma seperated, single line). A book title can only be added to the list once (no duplication)

* Searching a book: The user enters a term and the program must search the term within titles, authors 
  and publishers and report the existence of such a book with the requested term.
  - Create a function called: `search_book(books, term)` which will True or False on a match or not
* use a list of dictionaries for datastorage with the following attribute fields: [title, author, publisher, pub_date]
* create a menu structure that asks for the option to perform (A = add book, S = Search book, E = Exit (and print))
'''

#Implement a Python program that collects book information. The program starts with three options: 
# entering new book, searching a book, exit.

#* Entering new book: The program will ask to enter: book title, book author, publisher, publication date.
#  Input will be (comma seperated, single line). A book title can only be added to the list once (no duplication)

#* Searching a book: The user enters a term and the program must search the term within titles, authors
#  and publishers and report the existence of such a book with the requested term.
#  - Create a function called: `search_book(books, term)` which will True or False on a match or not
#* use a list of dictionaries for datastorage with the following attribute fields: [title, author, publisher, pub_date]
#* create a menu structure that asks for the option to perform (A = add book, S = Search book, E = Exit (and print))

def search_book(books, term):
    for book in books:
        if term in book['title'] or term in book['author'] or term in book['publisher']:
            return True
    return False

def main():
    books = []
    while True:
        print("A = add book, S = Search book, E = Exit")
        option = input("Select an option: ")
        if option == "A":
            title, author, publisher, pub_date = input("Enter book title, author, publisher, publication date: ").split(",")
            books.append({'title': title, 'author': author, 'publisher': publisher, 'pub_date': pub_date})
        elif option == "S":
            term = input("Enter search term: ")
            if search_book(books, term):
                print("Book found")
            else:
                print("Book not found")
        elif option == "E":
            #for loop books get values
            for book in books:
                print(book)
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()