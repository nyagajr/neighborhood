from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *


# Create your views here.
# @login_required(login_url='/accounts/login/')

def welcome(request):
    return render(request, 'welcome.html')

def signup(request):
    return redirect('/accounts/login/')
    return render(request, 'registration_form.html')

# def signup(request):
#     return redirect('/accounts/login/')
#     return render(request, 'registration_form.html')
