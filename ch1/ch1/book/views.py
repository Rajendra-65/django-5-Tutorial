from django.shortcuts import render,redirect
from book.forms import BookForm
from book.models import Book
from django.contrib import messages
# Create your views here.

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            print('hello')
            print(form.cleaned_data)
            messages.success(request,'Book added successfully!')
            return redirect('book_create')
        else:
            print("Form errors:",form.errors)
    else:
        form = BookForm()
    return render(request,'book/book_form.html',{'form':form})