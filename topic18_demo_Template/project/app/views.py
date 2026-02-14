from django.shortcuts import render

# Create your views here.
# Method hamesa capital me likhte h like POST,FILES 

def index(req):
    return render(req,'index.html')

def Registration(req):
    return render(req,'Registration.html')

def Register1(req):
    print("Hello...............")
    print(req.POST)
    print(req.FILES)
    # print(req.META)
    # print(req.Settings)
    n=req.POST.get('name')
    e=req.POST.get('email')
    c=req.POST.get('contact')
    p=req.POST.get('password')
    ph=req.FILES.get('photo')
    v=req.FILES.get('video')
    a=req.FILES.get('audio')
    d=req.FILES.get('resume')
    g=req.POST.get('gender')
    q=req.POST.getlist('qualification')
    s=req.POST.get('state')
    print(n,e,c,p,ph,v,a,d,g,q,s,sep=',')
    # cookie content
    response = render(req,'Login.html')
    response.set_cookie('name',n,max_age=10)
    response.set_cookie('email',e,max_age=20)
    response.set_cookie('contact',c,max_age=30)
    response.set_cookie('password',p,max_age=40)
    response.set_cookie('photo',ph)
    response.set_cookie('video',v)
    response.set_cookie('audio',a)
    response.set_cookie('resume',d)
    response.set_cookie('gender',g)
    response.set_cookie('qualification',q)
    response.set_cookie('state',s)
    return response

def Login(req):
    return render(req,'Login.html')

def get_cookie(req):
    print(req.COOKIES)
    n=req.COOKIES.get('name')
    e=req.COOKIES.get('email')
    c=req.COOKIES.get('contact')
    p=req.COOKIES.get('password')
    ph=req.COOKIES.get('photo')
    v=req.COOKIES.get('video')
    a=req.COOKIES.get('audio')
    d=req.COOKIES.get('resume')
    g=req.COOKIES.get('gender')
    q=req.COOKIES.get('qualification')
    s=req.COOKIES.get('state')
    print(n,e,c,p,ph,v,a,d,g,q,s,sep=',')

def delete_cookie(req):
    response = render(req,'Login.html')
    response.delete_cookie('name')
    response.delete_cookie('email')
    response.delete_cookie('contact')
    return response
    
        

