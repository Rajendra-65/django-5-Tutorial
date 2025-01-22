from django.urls import path,include
from student.views import all_data,single_data,registration,logIn,address,test,demo_form

urlpatterns = [
    path('all/',all_data,name='all'),
    path('single_data',single_data,name='single_data'),
    path('register/',registration,name='register'),
    path('logIn/',logIn,name='logIn'),
    path('address/',address,name='address'),
    path('test/',test,name='test'),
    path('demo-form/',demo_form,name='demo-form')
]
