from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')

def registration(req):
    return render(req,'registration.html')

def set_cookie_data(req):
    print('printing data in dict format')
    print(req.POST)
    print(req.FILES)
    print('printing values only')
    n=req.POST.get('name')
    e=req.POST.get('email')
    c=req.POST.get('contact')
    p=req.POST.get('password')
    ph=req.FILES.get('photo')
    a=req.FILES.get('audio')
    v=req.FILES.get('video')
    d=req.FILES.get('resume')
    g=req.POST.get('gender')
    s=req.POST.get('state')
    q=req.POST.getlist('qualification')
    print(n,e,c,p,ph,a,v,d,g,s,q,sep=',')
    # setting form data in cookies
    response = render(req,'login.html')
    response.set_cookie('name',n)
    response.set_cookie('email',e)
    response.set_cookie('contact',c)
    response.set_cookie('password',p)
    response.set_cookie('photo',ph)
    response.set_cookie('audio',a)
    response.set_cookie('video',v)
    response.set_cookie('resume',d)
    response.set_cookie('gender',g)
    response.set_cookie('state',s)
    response.set_cookie('qualification',q)
    return response

def get_cookie(req):
    print(req.COOKIES)
    n=req.COOKIES.get('name') 
    e=req.COOKIES.get('email') 
    c=req.COOKIES.get('contact') 
    p=req.COOKIES.get('password') 
    ph=req.COOKIES.get('photo') 
    a=req.COOKIES.get('audio') 
    v=req.COOKIES.get('video') 
    d=req.COOKIES.get('resume') 
    g=req.COOKIES.get('gender') 
    s=req.COOKIES.get('state') 
    q=req.COOKIES.get('qualification')
    data = {'name':n,'email':e,'contact':c,'password':p,'photo':ph,'audio':a,'video':v,'resume':d,'gender':g,'state':s,'qualification':q}
    return render(req,'login.html',data) 

def delete_cookie(req):
    response = render(req,'login.html')
    response.delete_cookie('name')
    response.delete_cookie('email')
    response.delete_cookie('contact')
    response.delete_cookie('password')
    response.delete_cookie('photo')
    response.delete_cookie('audio')
    response.delete_cookie('video')
    response.delete_cookie('resume')
    response.delete_cookie('gender')
    response.delete_cookie('state')
    response.delete_cookie('qualification')
    return response
