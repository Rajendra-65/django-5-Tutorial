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
from django.urls import path,include
from app1 import views as ap1
from app2 import views as ap2
from course import views as course
from student import views as student
from modelForm import views as mf
from book import views as book
# from app1.views import home,myapp1,myfunction
# from app2.views import myapp2,myapp2_me

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/",include("django_browser_reload.urls")),
    path('',include('app1.urls')),
    path('',include('app2.urls')),
    path('course/',include('course.urls')),
    path('',include('core.urls')),
    path('student/',include('student.urls')),
    path('modelForm/',include('modelForm.urls')),
    path('book/',include('book.urls')),
]
