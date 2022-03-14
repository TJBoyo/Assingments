 #You are to create a Library management system. 
 # An admin can add books, remove books, view all the borrowed book. 
 # A user can view all the books, search through the books by the name of the book, author, genre, category etc. 
 # A user can also borrow a book and all the borrowed books should be removed from where the books are and
 # added to the borrowed collection type. 
 # The copies of books available should also be added. 
 # If there's a book with no copies available the admin should be notified..


#Utilities
def display_books(library: list ) -> None:    
    """This function displays all the books"""
    not_availble  = 0
    for book in library:
        status = book['status']
        quantity = book['quantity']
        num_borrowed = int(status[0])
        if num_borrowed == quantity:
            not_availble += 1
            continue
        print('======================')
        print("Title:", book['title']) 
        print('Author', book['author'])
        print('Quantity', quantity - num_borrowed)
        print('Category', book['category'])
        print('========================')

    if not_availble == len(library):
        print('No availabe books')


def book_select(book: dict) -> None:
    """This function is used to display the boks from a search"""
    print('======================')
    print("Title:", book['title']) 
    print('Author', book['author'])
    print('Quantity', book['quantity'] - int(book['status'][0]))
    print('Category', book['category'])
    print('======================')
    if book['quantity'] - int(book['status'][0]) == 0 :
        print('No Available Copy in Stock')

def pick_a_book():
    select = int(input('Enter the required number :'))
    if select == 1:
        title = input("What is the title of the book you would like to find? ")
        for book in library:
            if book['title'] == title:
                #print(book)
                book_select(book=book)          
            
    elif select == 2:
        author = input("Who is the author of the book you would like to find? ")
        for book in library:
            if book['author'] == author:
                #print(book)
                book_select(book=book)  
            
    else:
        category = input("What is the category of the book you would like to find? ")
        for book in library:
            if book['category'] == category:
                #print(book)
                book_select(book=book)
def display_books1(library: list ) -> None:    
    """This function displays all the books"""
    not_availble  = 0    
    for book in library:
        status = book['status']
        quantity = book['quantity']
        num_borrowed = int(status[0])
        rem_books = quantity - num_borrowed
        if rem_books < quantity:
            #select = int(input('Enter the required number :'))
            pick_a_book()

        # if num_borrowed == quantity:
        #     not_availble += 1
      
            continue
        print('======================')
        print("Title:", book['title']) 
        print('Author', book['author'])
        print('Rem Quantity', rem_books)
        print('Quantity', quantity - num_borrowed)
        print('Category', book['category'])
        print('========================')

    if not_availble == len(library):
        print('No availabe books')

#MIAN PROGRAM
library = [
    {'title': 'Abc', 'author':'john', 'quantity':2, 'category':'case steller', 'status' : '2-Borrowed'},
]
library.append({'title' : 'thing fall apart', 'author' : 'Chinua', 'quantity' : 4, 'category' : 'Horror', 'status' : '1-Borrowed'})
library.append({'title' : 'Brave heart', 'author' : 'Mel', 'quantity' : 1, 'category' : 'Adventure', 'status' : '1-Borrowed'})

display_books1(library=library)
#Display all books
display_books(library=library)       

# Search for books
print("How would you like to search for your book?")
print("1. Title   2.Author 3.Category")

pick_a_book()






           





