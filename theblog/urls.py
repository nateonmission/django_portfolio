from django.contrib import admin
from django.urls import path, include
from .views import blog_home

urlpatterns = [
    path('blog_home/', blog_home, name='blog_home')
]