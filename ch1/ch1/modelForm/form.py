from django import forms
from student.models import Profile

class Registration(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','city']
        lables= {
            'name':'Enter name',
            'email':'Enter email',
            'city':'City Name'
        }
        error_messages = {
            'email':{'required':'Email is required'}
        }
        widgets = {
            'password' : forms.PasswordInput(attrs={
                'class':'pwdclass'
            })
        }