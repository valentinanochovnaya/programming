from django.urls import path
from .imports import views

url_patterns = [
    path('', views.freelancersList, name='freelancers')
]