from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE )

    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField('Book')

    def __str__(self):
        return self.name
    

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField('Library', on_delete= models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),

    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Member'
    )

    def __str__(self):
        return self.user.username
    
    
    







