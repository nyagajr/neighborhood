from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
# @login_required(login_url='/accounts/login/')

def welcome(request):
    return render(request, 'welcome.html')

# def signup(request):
#     return redirect('/accounts/login/')
#     return render(request, 'registration_form.html')
