from django.db import models

# Create your models here.
class Book(models.Model):

#     title: CharField with a maximum length of 200 characters.
# author: CharField with a maximum length of 100 characters.
# publication_year: IntegerField.

    title = models.CharField(max_length=200, null=False)
    author  =  models.CharField(max_length=100, null=False)
    publication_year = models.IntegerField(null=False)



    def __str__(self):
        return f"title = {self.title}: author = {self.author}"