from django import forms
from book.models import Book

class BookForm(forms.ModelForm):
    class Meta:
         model = Book
         fields = '__all__'

         widgets = {
              'title' : forms.TextInput(attrs ={
                   'class' : 'w-full',
                   'placeholder' : 'Enter book title'
              }),
              'author': forms.TextInput(attrs = {
                   'class':'w-full',
                   'placeholder' : 'Enter author name'
              }),
              'description': forms.Textarea(attrs = {
                   'class':'w-full',
                   'rows':4,
                   'placeholder': 'Enter book description'
              }),
              'genre': forms.Select(attrs={
                   'class':'w-full'
              }),
              'isbn': forms.TextInput(attrs={
                   'class':'w-full',
                   'placeholder':'Enter isbn'
              }),
              'publication_date' : forms.DateInput(attrs={
                   'class':'w-full',
                   'placeholder':'Enter publication date'
              })
         }