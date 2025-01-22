from django import forms

class Registration(forms.Form):
    #UnderScore becomes " " in forms
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()

class loginn(forms.Form):
    #UnderScore becomes " " in forms
    email = forms.EmailField()
    password = forms.CharField()

class Address(forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.IntegerField()

class Test(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()