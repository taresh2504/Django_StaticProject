from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req,'index.html')

def landing(req):
    return render(req,'landing.html')

def home(req):
    return render(req,'home.html')
