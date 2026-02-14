from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.

def first(req):
    return render(req,'index.html')

def httpresponse(req):
    return HttpResponse('httpresponse is working')

def jsonresponse(req):
    data = ('json working successfully',10,3.14,True)
    return JsonResponse(data,safe=False)

def render1(req):
    return render(req,'home.html',{'info':'render working successfully'})

def back(req):
    return render(req,'index.html')

def redirect1(req):
    return redirect('https://www.instagram.com/')
