from django.shortcuts import render
from django.views import View
from .models import Book
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm


@method_decorator(permission_required('bookshelf.can_view_book', raise_exception=True), name='dispatch')
class ViewBooks(View):
    def get(self, request):
        book_list = Book.objects.all()
        context = {
            "book_list": book_list
        }
        return render(request, 'book_list.html', context)
    
class AddBook(View):
    def get(self, request):
        form = ExampleForm()  # This ensures ExampleForm is used
        return render(request, 'bookshelf/example_form.html', {'form': form})