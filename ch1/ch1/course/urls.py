from django.urls import path
from course.views import php_course,learn_django,fast_api

urlpatterns = [
    path('php/',php_course),
    path('learn-django',learn_django),
    path('fast_api',fast_api)
]
