import os
import json
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import stripe
from django.contrib.auth import login
from django.contrib.auth.models import User
# from . import models


DOMAIN = "http://localhost:8000"  # Move this to your settings file or environment variable for production.
stripe.api_key = os.environ['STRIPE_SECRET_KEY']

def home(request) :
    return render(request, 'home.html' )

def projects(request) :
    return render(request, 'projects.html' )

def open_source(request) :
    return render(request, 'open_source.html' )

def resume(request) :
    return render(request, 'resume.html' )