from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def contact(req):
    data = {
        'name':'Taresh Kumar Tandey',
        'email':'taresh25202@gmail.com',
        'demo' : 'this is django class',
        'l': ['python',10,'java','php']
    }
    data1 = [
        {'name':'Taresh','email':'taresh25202@gmail.com'},
        {'name':'Priyesh','email':'priyesh@gmail.com'},
        {'name':'Krish','email':'krish@gmail.com'},
        {'name':'Tanish','email':'tanish@gmail.com'},
    ]
    return render(req,'contact.html',{'data':data,'xyz':data1})