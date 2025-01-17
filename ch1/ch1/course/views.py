from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def php_course(request):
    return HttpResponse(f'<h1>Learn PHP Step by Step</h1>')

def learn_django(request):
    # return render(req,template_name,context=dic_name,content_type=mime_type,status=none,using=none)
    seats = 10
    coursename = {
        'cname':'Django',
        'st':seats
    }
    return render(request,'course/django.html',coursename)

def fast_api(request):
    return render(request,'course/fastapi.html')