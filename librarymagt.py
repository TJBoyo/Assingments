 #You are to create a Library management system. 
 # An admin can add books, remove books, view all the borrowed book. 
 # A user can view all the books, search through the books by the name of the book, author, genre, category etc. 
 # A user can also borrow a book and all the borrowed books should be removed from where the books are and
 # added to the borrowed collection type. 
 # The copies of books available should also be added. 
 # If there's a book with no copies available the admin should be notified..



library = [
    {'title': 'Abc', 'author':'john', 'quantity':2, 'category':'case steller', 'status' : '2-Borrowed'},
]

library.append({'title' : 'thing fall apart', 'author' : 'Chinua', 'quantity' : 4, 'category' : 'Horror', 'status' : '1-Borrowed'})
library.append({'title' : 'Brave heart', 'author' : 'Mel', 'quantity' : 1, 'category' : 'Adventure', 'status' : '1-Borrowed'})

def display_books():    
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

display_books()       
for book in library:
    status = book['status']
    quantity = book['quantity']
    num_borrowed = int(status[0])
print("How would you like to search for your book?")
print("1. Title   2.Author 3.Category")
select = int(input('Enter the required number :'))

if select == 1:
    title = input("What is the title of the book you would like to find? ")
    for book in library:
        if book['title'] == title:
            print(book)
            break
elif select == 2:
    author = input("Who is the author of the book you would like to find? ")
    for book in library:
        if book['author'] == author:
            print(book)
            break
else:
    category = input("What is the category of the book you would like to find? ")
    for book in library:
        if book['category'] == category:
            print(book)
            break
print('======================')
print("Title:", book['title']) 
print('Author', book['author'])
print('Quantity', quantity - num_borrowed)
print('Category', book['category'])
print('======================')

if quantity - num_borrowed == 0 :
    print('No Available Copy in Stock')



