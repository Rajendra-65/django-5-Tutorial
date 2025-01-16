from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myapp2(request):
    return HttpResponse('my App 2 page')

def myapp2_me(request):
    return HttpResponse('myapp2-Me')

def kwargs_in_django(request,**kwargs):
    status = kwargs.get('status','Not allowed')
    print(status)
    return HttpResponse(f'<h1>Hello Django{status}</h1>')