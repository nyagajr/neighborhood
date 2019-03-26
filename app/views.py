from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.
@login_required(login_url='/accounts/login/')

def welcome(request):
    new = Hood.objects.all()
    return render(request, 'welcome.html',locals())

def signup(request):
    return redirect('/accounts/login/')
    return render(request, 'registration_form.html')

def profile(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =UploadForm()

        profile = Profile.objects.all()
        all_profile = Profile.objects.all()
    return render(request,'profile.html', locals())

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Hood.search_by_hood_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_articles": searched_articles})

    else:
        message = "please enter a name"
        return render(request, 'search.html',{"message":message})


# def signup(request):
#     return redirect('/accounts/login/')
#     return render(request, 'registration_form.html')
