from django.contrib import admin
from .models import Book, CustomUser
# Register your models here.

admin.register(CustomUser)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=( "title", "author", "publication_year")
    list_filter = ('title', 'author')
    search_fields = ['title', 'author']



