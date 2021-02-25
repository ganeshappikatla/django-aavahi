from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    return render(request,'login.html')

def existinguserpage(request):
    return render(request,'existinguserpage.html')

def portfoliopage(request):
    return render(request,'portfoliopage.html')

def verificationpage(request):
    return render(request,'verificationpage.html')



