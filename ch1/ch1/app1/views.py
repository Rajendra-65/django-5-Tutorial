from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myfunction(request):
    return HttpResponse('Hello Django')

def home(request):
    return HttpResponse('Home page')

def learn_python(request):
    return HttpResponse('learning python')

def myapp1(request):
    return HttpResponse('My App 1 page')