from django.urls import include, path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('', views.lists_books, name="index"),
    path('library/books', views.LibraryDetailView.as_view(), name=" books_in_library"),
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('admin-view', views.admin_view,name= 'admin' ),
    path('librarian-view', views.librarian_view ,name= 'librarian' ),
    path('member-view', views.member_view ,name= 'member' )

]

