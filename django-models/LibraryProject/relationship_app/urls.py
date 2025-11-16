from django.urls import include, path
import . import views

path('', views.lists_all_books, name="index")
path('', views.DetailViewOfLibrary, name=" books_in_library")
