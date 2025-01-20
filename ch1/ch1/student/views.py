from django.shortcuts import render
from student.models import Profile
from student.forms import Registration,loginn
# Create your views here.

def all_data(req):
    all_students = Profile.objects.all()
    print(all_students)
    return render(req,'student/all.html',{'students':all_students})

def single_data(req):
    student = Profile.objects.get(id=1)
    print(student)
    return render(req,'student/single.html',{'student':student})

# def register(req):
#     return render(req,'student/registration.html')

def registration(req):
    form = Registration(field_order=['email','city'],auto_id=True)
    return render(req,'student/registration.html',{'form':form})

def logIn(req):
    form = loginn()
    return render(req,'student/login.html',{'form':form})