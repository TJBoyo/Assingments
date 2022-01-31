books = ['a', 'b', 'c']
authours = ['James', 'Ben', 'Sarah']

number_elements = len(books)

for i in range(number_elements):
    book = books[i]
    author = authours[i]
    display = f"'{book}' was written by {author}"
    print(display)

name_search = input('what book are you looking for?')
if name_search in books:
    i = books.index(name_search)
    author = authours[i]
    print(f"{name_search} was written by {author}")


word = "This is a simple@quiz but what@want is this: me@gmail.com"
word_required = word.split(':')
print(word_required[1].strip())

