from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myfunction(request):
    return HttpResponse('Hello Django')

def home(request):
    return HttpResponse('Home page')

def learn_python(request,**kwargs):
    status = kwargs.get('status','Not Allowed')
    print(status)
    return HttpResponse(f'<h1>Hello I am Learning python status {status}</h1>')

def myapp1(request):

    return HttpResponse('My App 1 page')