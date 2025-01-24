from django.urls import path
from modelForm.views import register

urlpatterns = [
    path('register',register,name="register")
]
