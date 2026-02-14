from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def set_session(req):
    return render(req,'register.html')

def set_session_data(req):
    print(req.POST)
    print(req.FILES)
    n = req.POST.get('name')
    e = req.POST.get('email')
    c = req.POST.get('contact')
    p = req.POST.get('password')
    ph = req.POST.get('photo')
    a = req.POST.get('audio')
    v = req.POST.get('video')
    d = req.POST.get('resume')
    s = req.POST.get('state')
    q = req.POST.getlist('qualification')
    g = req.POST.get('gender')
    req.session['name']=n
    req.session['email']=e
    req.session['contact']=c
    req.session['password']=p
    req.session['photo']=ph
    req.session['audio']=a
    req.session['video']=v
    req.session['resume']=d
    req.session['state']=s 
    req.session['qualification']=q 
    req.session['gender']=g
    return render(req,'landing.html')

def get_session(req):
    n=req.session.get('name')
    e=req.session.get('email')
    c=req.session.get('contact')
    p=req.session.get('password')
    ph=req.session.get('photo')
    a=req.session.get('audio')
    v=req.session.get('video')
    d=req.session.get('resume')
    s=req.session.get('state')
    g=req.session.get('gender')
    q=req.session.get('qualification')
    data = {'name':n,'email':e,'contact':c,'password':p,'photo':ph,'audio':a,'video':v,'resume':d,'state':s,'gender':g,'qualification':q}
    return render(req,'landing.html',data)

def delete_session(req):
    # req.session.pop('name')
    # del req.session['email']
    req.session.flush()
    return render(req,'landing.html')

def sqlitedata(req):
    n = req.POST.get('name')
    e = req.POST.get('email')
    c = req.POST.get('contact')
    p = req.POST.get('password')
    ph = req.POST.get('photo')
    a = req.POST.get('audio')
    v = req.POST.get('video')
    d = req.POST.get('resume')
    s = req.POST.get('state')
    q = req.POST.getlist('qualification')
    g = req.POST.get('gender')
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

def login(req):
    return render(req,'login.html')
