from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def php_course(request):
    return HttpResponse(f'<h1>Learn PHP Step by Step</h1>')

def learn_django(request):
    return HttpResponse('<h1>Hello Django from course App</h1>')