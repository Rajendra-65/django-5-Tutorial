from django.shortcuts import render
from student.models import Profile
from student.forms import Registration,loginn,Address,Test,DemoForm
from django.http import HttpResponseRedirect
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

def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            print(first_name,last_name,email,city)
            return HttpResponseRedirect('/student/success')
    else:
        form = Registration()
    return render(request,'student/registration.html',{'form':form})

def logIn(req):
    form = loginn()
    return render(req,'student/login.html',{'form':form})

def address(req):
    fm = Address()
    return render(req,'student/address.html',{'form':fm})

def test(req):
    test = Test()
    return render(req,'student/test.html',{'test':test})

def demo_form(req):
    form = DemoForm()
    return render(req,'student/demo.html',{'form':form})

def success(req):
    return render(req,'student/success.html')