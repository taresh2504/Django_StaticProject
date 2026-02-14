from django.shortcuts import render,redirect
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.
def my_render(req):
    # return render(req,'index.html',{'n':'Taresh'})
    data = {'n':'taresh'}
    return render(req,'index.html',data)

# def my_redirect(req):
#     return redirect('redirect1',x=10)

def my_redirect(req):
    url = reverse('redirect2')
    data = urlencode({'n':"Taresh"})
    return redirect(f'{url}?{data}')

def redirect1(req,x):
    return render(req,'index.html',{'data':x})

def redirect2(req):
    name = req.GET.get('n')
    # print(name)
    return render(req,'index.html',{'data':name})