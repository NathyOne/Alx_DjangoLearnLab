from django.shortcuts import render
from django.views import View
from .models import Book
# Create your views here.
from django.contrib.auth.decorators import permission_required
@permission_required('can_view', raise_exception=True)
class ViewBooks(View):
    book_lists = Book.objects.all()
    context = {
        "book_lists":book_lists
    }
    