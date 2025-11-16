from django.shortcuts import render, redirect

from .models import Book, Author, Librarian, Library
from .models import Library
from django.views.generic.detail import DetailView
from .forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def lists_books(request):
    book_list = Book.objects.all()

    context  = {
                "book_list" : book_list
    }
    return render(request, "relationship_app/list_books.html", context=context)

class LibraryDetailView(DetailView):
    # all_books_in_the_Library = Library.objects.get(name="main library").books.all()
    all_books_in_library = Book.objects.filter(library__name="Main Library")
    template_name =  "relationship_app/library_detail.html"



# views for user login, logout, and registration.

def Registration(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "registration successfull")
    else:
        form = UserCreationForm()

    
    return render(request, 'relationship_app/register.html', {'form': form})




class Login(View):

    template_name = 'login.html'
    @method_decorator(csrf_protect)
    def get(self, request):

        if request.user.is_authenticated:
            return redirect('')
        render(request, self.template_name)


    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(user, request)

            messages.success(request, "login successfull")
            next_page = request.GET.get('next' , '')
            return redirect(next_page)
        else:
            # Login failed
            messages.error(request, 'Invalid username or password.')
            return render(request, self.template_name, {
                'username': username  # Pre-fill username field
            })
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('login')
    
    def post(self, request):  # For POST requests (more secure)
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('login')
    
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test



@user_passes_test(
    lambda user: user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin',
    login_url='/login/'
) 
def admin_view(request):
    context = {
        'title': 'Admin Dashboard',
        'user': request.user,
        'role': request.user.userprofile.role,
    }
    return render(request, 'admin_view.html', context)



@user_passes_test(
    lambda user: user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarians',
    login_url='/login/'
)
def librarian_view(request):
    context ={
        'title': 'Librarian Dashboard', 
        'user': request.user,
        'role': request.user.userprofile.role,
    }
    return render(request, 'librarian_view.html', context)


@user_passes_test(
    lambda user: user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Members',
    login_url='/login/'
)
def member_view(request):
    context ={
        'title': 'Member Dashboard', 
        'user': request.user,
        'role': request.user.userprofile.role,
    }
    return render(request, 'member_view.html', context)



class member_view(View):
    pass




    

        


    
