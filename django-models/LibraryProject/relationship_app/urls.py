from django.urls import include, path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', views.lists_books, name="index"),
    path('library/books', views.LibraryDetailView.as_view(), name=" books_in_library"),
]

