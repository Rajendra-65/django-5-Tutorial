from django.contrib import admin
from django.urls import path
from app1.views import myfunction,myapp1,learn_python

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myfunction/',myfunction),
    path('myapp1/',myapp1),
    path('py/',learn_python,kwargs={'status':'OK'})
]