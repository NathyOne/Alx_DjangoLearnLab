from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, date_of_birth, profile_picture, **extra_fields):
        if not email:
            raise ValueError('users  must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            date_of_birth = date_of_birth,
            profile_picture = profile_picture,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        USERNAME_FIELD = 'email'

        return user
    def create_superuser(self, username, password, date_of_birth, profile_picture, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username,password=password,**extra_fields)

        

#     title: CharField with a maximum length of 200 characters.
# author: CharField with a maximum length of 100 characters.
# publication_year: IntegerField.

    title = models.CharField(max_length=200, null=False)
    author  =  models.CharField(max_length=100, null=False)
    publication_year = models.IntegerField(null=False)



    def __str__(self):
        return f"title = {self.title}: author = {self.author}"