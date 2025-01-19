from django.contrib import admin
from django.urls import path,include
from student.views import all_data,single_data

urlpatterns = [
    path('all/',all_data,name='all'),
    path('single_data',single_data,name='single_data')
]
