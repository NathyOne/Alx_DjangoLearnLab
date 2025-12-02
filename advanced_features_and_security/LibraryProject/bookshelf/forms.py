from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Include fields from your Book model
        
        # Optional: Add widgets, labels, help_text, etc.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Book Author',
        }