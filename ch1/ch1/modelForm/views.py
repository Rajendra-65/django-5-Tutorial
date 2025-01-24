from django.shortcuts import render
from modelForm.form import Registration

# Create your views here.

def register (request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            city = form.cleaned_data['city']
            print(nm,em,city)
    else:
        form = Registration()
    return render(request,'student/register.html',{"form":form})