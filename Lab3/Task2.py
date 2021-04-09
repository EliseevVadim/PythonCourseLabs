from classes.for2ndTask import Book, Library
lib = Library(1, 'somewhere')
lib+=Book('Leo Tolstoi', 'War and Peace')
lib+=Book('Charles Dickens', 'David Copperfield')
for book in lib:
    print(book)
    print(book.tag())