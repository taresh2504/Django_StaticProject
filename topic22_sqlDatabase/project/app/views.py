from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def index(req):
    return render(req,'index.html')

def register(req):
    return render(req,'register.html')

def login(req):
    return render(req,'login.html')

def sqlitedata(req):
    n=req.POST.get('name')
    e=req.POST.get('email')
    c=req.POST.get('contact')
    p=req.POST.get('password')
    ph=req.FILES.get('photo')
    a=req.FILES.get('audio')
    v=req.FILES.get('video')
    d=req.FILES.get('resume')
    q=req.POST.getlist('qualification')
    g=req.POST.get('gender')
    s=req.POST.get('state')
    Employee.objects.create(
        Name=n,
        Email=e,
        Contact=c,
        Password=p,
        Photo=ph,
        Audio=a,
        Video=v,
        Resume=d,
        State=s,
        Qualification=q,
        Gender=g
    )
    return redirect('login')

