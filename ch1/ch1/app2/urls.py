from django.contrib import admin
from django.urls import path
from app2.views import myapp2,myapp2_me,kwargs_in_django

urlpatterns = [
    path('myapp2/',myapp2),
    path('myapp2_me/',myapp2_me),
    path('kwargs_in_django/',kwargs_in_django,kwargs={'status':'OK'})
]