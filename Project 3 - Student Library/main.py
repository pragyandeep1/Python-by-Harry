''' Implement a student library system using oops where a student can borrow a book from a list of books.
Create a separate library and student class. Your program must be menu driven.
You are free to choose methods and attributes of your choice to implement this functionality.'''

class Library:
    def __init__(self, lob):
        self.books = lob
        
    def disp(self):
        print('The present books in the library are ')
        for book in self.books:
            print('*' +book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You are issued {bookName}. Kindly return the book on time.")
            self.books.remove(bookName)
            return True
        else:
            print("This book is out of stock.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("We got the book. Have a nice day! Thank you.")

class Student:
    def reqBook(self):
        self.book = input("Enter the name of the book to be borrowed: ")
        return self.book

    def retBook(self):
        self.book = input("Enter the name of the book to be returned: ")
        return self.book

if __name__ is '__main__':
    cent = Library(['alfo', 'django', 'clrs', 'python'])
    # cent.disp()
    stud = Student
    while(True):
        welcom = '''WELCOME TO THE CENTRAL LIBRARY
        Kindly Select a choice:
        1. List of all books
        2. Boorow a book
        3. Return a book
        4. Exit
        '''
        a = int(input("Enter an option: "))
        if a is 1:
            cent.disp()
        elif a is 2:
            cent.borrowBook()
        elif a is 3:
            cent.borrowBook()
        elif a is 4:
            cent.borrowBook()
        elif a is 5:
            print('Have a great day!')
            exit()
        else:
            print('Invalid entry')
        print(welcom)