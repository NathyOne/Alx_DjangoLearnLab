from django.urls import include, path
from . import views
from .views import lists_books, LibraryDetailView

urlpatterns = [
    path('', views.lists_books, name="index"),
    path('library/books', views.LibraryDetailView.as_view(), name="books_in_library"),
    path('register/', views.Registration, name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

]

