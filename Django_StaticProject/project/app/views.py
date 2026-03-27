from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def account(req):
    return render(req,'landing.html',{'account':True})

def search(req):
    return render(req,'landing.html',{'search':True})

def bag(req):
    return render(req,'landing.html',{'bag':True})

def shopbycategory(req):
    return render(req,'shopbycategory.html')
