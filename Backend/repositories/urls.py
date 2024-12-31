# repositories/urls.py
from django.urls import path
from .views import get_repositories, get_languages

urlpatterns = [
    path('repositories/', get_repositories, name='repositories'),
    path('languages/', get_languages, name='languages'),
]
