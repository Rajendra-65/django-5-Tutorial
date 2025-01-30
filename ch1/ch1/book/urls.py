from django.urls import path
from book import views

urlpatterns = [
    path('new/', views.book_create, name='book_create'),
]