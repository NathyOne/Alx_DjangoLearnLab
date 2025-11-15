from .models import Book, Author, Librarian, Library

book_by_specific_author = Book.objects.filter(Author='James')
allBooks = Book.objects.all()
librarian_for_library = Librarian.objects.filter(Library = "Abrehot")