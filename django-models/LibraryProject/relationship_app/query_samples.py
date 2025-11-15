from .models import Book, Author, Librarian, Library
#   LibraryProject/relationship_app/query_samples.py doesn't contain: ["Library.objects.get(name=library_name)", "books.all()"]

book_by_specific_author = Book.objects.filter(name=Author.name)
allBooks = Book.objects.all()
librarian_for_library = Librarian.objects.get(library__name = "Abrehot")