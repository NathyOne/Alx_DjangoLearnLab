from django.shortcuts import render
from django.req import request 
from .models import Book, Author, Librarian, Library
from django.views import generic

# Create your views here.
def lists_all_books(request):
    book_list = Book.objects.all()

    context  = {
                "book_list" : book_list
    }
    return render(request, "relationship_app/list_books.html", context=context)


#Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
# Utilize Django’s ListView or DetailView to structure this class-based view.
class DetailViewOfLibrary(generic.DetailView):
    all_books_in_the_Library = Library.objects.get(name="main library").books.all()
    all_books_in_library = Book.objects.filter(library__name="Main Library")


    
