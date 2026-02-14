from django.shortcuts import render     # render,redirect ek module m hai 
from django.shortcuts import redirect
from django.http import JsonResponse     #json.http response ek module me hai     
from django.http import HttpResponse

# Create your views here.

def landing(req):
    return render(req,'landing.html')

def json_response(req):
    # data = {'active1':True,
    #         "active2":False,
    #         '''active3''':None,
    #         }
    # data = 10  # non dict ko pass krna h to safe = False likhna padega
    # data = 'python'
    # data = [10,20,30,'python'] # chaahe list bhejo ya tuple result list m aayega
    # data = (10,20,30,'python')
    # data = {10,20,30,'python'} # does not support set,frozen set in json 
    # data = True 
    # fundamental data types = 5 hote h
    data = None
    return JsonResponse(data,safe=False)
