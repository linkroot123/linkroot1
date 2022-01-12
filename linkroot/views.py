# I created this file
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'registration.html')
    
def forgot(request):
    return render(request, 'forgotpassword.html')

def index(request):
    return render(request, 'index.html')
