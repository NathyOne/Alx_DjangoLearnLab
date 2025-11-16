from django.shortcuts import render
from .models import Book, Author, Librarian, Library
/from .models import Library
from django.views.generic.detail import DetailView
# Create your views here.
def lists_books(request):
    book_list = Book.objects.all()

    context  = {
                "book_list" : book_list
    }
    return render(request, "relationship_app/list_books.html", context=context)


#Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
# Utilize Django’s ListView or DetailView to structure this class-based view.
class LibraryDetailView(DetailView):
    # all_books_in_the_Library = Library.objects.get(name="main library").books.all()
    all_books_in_library = Book.objects.filter(library__name="Main Library")
    template_name =  "relationship_app/library_detail.html"


    
