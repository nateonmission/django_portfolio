"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from .views import home, projects, open_source, resume

urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects, name='projects'),
    path('open_source/', open_source, name='open_source'),
    path('resume/', resume, name='resume'),
    path('admin/', admin.site.urls, name='admin'),
    path('', include('products.urls')),
    path('', include('theblog.urls')),
]

