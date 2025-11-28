from django.contrib import admin
from .models import  CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display=( "title", "author", "publication_year")
#     list_filter = ('title', 'author')
#     search_fields = ['title', 'author']



