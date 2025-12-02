from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email=email, password=password, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
 
 
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='profile_photos/')
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    
class Book(models.Model):
#     title: CharField with a maximum length of 200 characters.
# author: CharField with a maximum length of 100 characters.
# publication_year: IntegerField.

    title = models.CharField(max_length=200, null=False)
    author  =  models.CharField(max_length=100, null=False)
    publication_year = models.IntegerField(null=False)




    def __str__(self):
        return f"title = {self.title}: author = {self.author}"
    class Meta:
        permissions=[
            ('can_publish', 'can publish a book'),
            ('can_edit', 'can edit a book'),
            ('can_view', 'can view a book'),
            ('can_create', 'can create a new book'),
            ('can_delete', 'can delete existing book'),
        ]