from django.shortcuts import render
from django.http import HttpResponse
import json

# json:- 
# 1. dumps() = python to json_data
# 2. loads() = json_data to python

# Create your views here.
def http_response(req):
    # return HttpResponse('hello http_response')
    # return HttpResponse('<h1>hello......</h1>')
    # return HttpResponse('<h1 style="color:red">hello......</h1>')
    # data = 'hlw'
    # return HttpResponse(data,content_type='text/plain')
    # data = '<h1 style="color:blue">hlw</h1>'
    # return HttpResponse(data,content_type='text/html')
    data = {'x':True,'y':False,'z':None}
    j_data = json.dumps(data)
    return HttpResponse(j_data,content_type='application/json')
    