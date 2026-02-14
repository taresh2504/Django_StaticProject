from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.
def httpresponse1(req):
    return HttpResponse('Http_response is working')

def httpresponse2(req):
    return HttpResponse('<h1>hello......</h1>')

def httpresponse3(req):
    return HttpResponse('<h1 style="color:red">hello......</h1>')

def httpresponse4(req):
    data = 'hlw'
    return HttpResponse(data,content_type='text/plain')

def httpresponse5(req):
    data = '<h1 style="color:blue">hlw</h1>'
    return HttpResponse(data,content_type='text/html')

def httpresponse6(req):
    data = {'x':True,'y':False,'z':None}
    j_data = json.dumps(data) 
    return HttpResponse(j_data,content_type='application/json')

# JSON Response Begin 

def jsonresponse1(req):
    data = {'active1':True,
            "active2":False,
            '''active3''':None,
            }
    return JsonResponse(data)

def jsonresponse2(req):
    data = 10
    return JsonResponse(data,safe=False)

def jsonresponse3(req):
    data = 'Taresh'
    return JsonResponse(data,safe=False)

def jsonresponse4(req):
    data = [10,20,'Django']
    return JsonResponse(data,safe=False)

def jsonresponse5(req):
    data = (5,15,'OOPS',3.14)
    return JsonResponse(data,safe=False)

def jsonresponse6(req):
    data = True
    return JsonResponse(data,safe=False)

def jsonresponse6(req):
    data = None
    return JsonResponse(data,safe=False)

# Render begin 

def render1(req):
    x = {'a':'Sanjay'}
    return render(req,'home.html',x)

def render2(req):
    a = 10
    b = True
    c = 'Render'
    d = 1.44444
    return render(req,'home.html',{'p':a,'q':b,'r':c,'s':d})

# Redirect begin 

def redirect1(req):
    return redirect('https://www.facebook.com/')

def redirect2(req):
    return redirect('first')

def redirect3(req):
    return render(req,'index.html')

def redirect4(req,x):
    return render(req,'index.html',{'data':x})

def redirect5(req,name,age,add):
    d = {
        'n':name,
        'a':age,
        'add':add
    }
    return render(req,'home.html',d)

def redirect6(req):
    url = reverse('redirect7')
    data = urlencode({'n':"Rahul"})
    return redirect(f'{url}?{data}')

def redirect7(req):
    name = req.GET.get('n')
    return render(req,'home.html',{'info':name})



