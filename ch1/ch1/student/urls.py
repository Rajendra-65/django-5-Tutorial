from django.urls import path,include
from student.views import all_data,single_data,registration,logIn

urlpatterns = [
    path('all/',all_data,name='all'),
    path('single_data',single_data,name='single_data'),
    path('register/',registration,name='register'),
    path('logIn/',logIn,name='logIn'),
]
