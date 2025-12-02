from django.shortcuts import render
from django.views import View
from .models import Book
# Create your views here.
from django.contrib.auth.decorators import permission_required

@permission_required('can_view', raise_exception=True)
class ViewBooks(View):
    books = Book.objects.all()
    context = {
        "books":books
    }