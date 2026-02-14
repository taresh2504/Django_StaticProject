from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')

def contact(req):
    data = {
        'name':'Taresh Tandy',
        'email':'taresh25202@gmail.com',
        'demo':'this is django DTL Filter',
        'l':['Python',3.14,10,'Java']
    }
    data1 = [
        {'name':'Taresh Tandy','email':'taresh25202@gmail.com'},
        {'name':'Krish gour','email':'krish@gmail.com'},
        {'name':'Priyesh Mishra','email':'priyesh@gmail.com'},
        {'name':'Tanish Parihar','email':'tanish@gmail.com'},
        {'name':'Smriti Jaiswaal','email':'smriti@gmail.com'},
        ]

    return render(req,'contact.html',{'info':data,'xyz':data1})
