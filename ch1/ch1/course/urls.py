from django.urls import path
from course.views import php_course,learn_django

urlpatterns = [
    path('php/',php_course),
    path('learn-django',learn_django)
]
