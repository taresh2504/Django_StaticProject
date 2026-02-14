from django.shortcuts import render,redirect

# Create your views here.
# def home(req,x):
#     return render(req,'home.html',{'data':x})

def home(req,name,age,add):
    d = {
        'n':name,
        'a':age,
        'ad':add
    }
    return render(req,'home.html',d)
