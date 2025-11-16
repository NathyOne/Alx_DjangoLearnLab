from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.lists_all_books, name="index"),
    path('library/books', views.DetailViewOfLibrary.as_view(), name=" books_in_library"),
]

