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

def book_list(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request,'book/book-list.html',{'books':books})

def book_detail(request,pk):
    book = Book.objects.get(pk = pk)
    return render(request, 'book/book_detail.html',{'book':book})

def book_update(request,pk):
    book = Book.objects.get(pk = pk)
    if request.method == "POST":
        form = BookForm(request.POST , instance = book)
        if form.is_valid():
            form.save()
            messages.success(request,'Book updated Successfully!')
            return redirect('book_list')
    else:
        form = BookForm(instance = book)
    return render(request,'book/book_form.html',{'form':form})

def book_delete(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request,'Book deleted successfully!')
    return redirect('book_list')