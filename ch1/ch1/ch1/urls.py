"""
URL configuration for ch1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as ap1
from app2 import views as ap2
# from app1.views import home,myapp1,myfunction
# from app2.views import myapp2,myapp2_me

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ap1.home,name='home'),
    path('myfun/',ap1.myfunction,name='myfunction'),
    path('py/',ap1.learn_python,name='learn_python'),
    path('app2/',ap2.myapp2,name='myapp2'),
    path('myapp2_me/',ap2.myapp2_me,name='myapp2_me'),
    path ('kwargs_in_django/',ap2.kwargs_in_django,kwargs={'status':'200'},name='kwargs_in_django')
]
