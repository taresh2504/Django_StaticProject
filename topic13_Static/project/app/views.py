from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def service(req):
    return render(req,'service.html')
