from django.shortcuts import render
from .models import Employee as Emp

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def all(req):
    all_data=Emp.objects.all()
    print(type(all_data))
    all_data=list(all_data.values())
    print(type(all_data))

    return render(req,'landing.html',{'data':all_data})

def filter(req):
    data = Emp.objects.filter(City='Agra')
    print(data)
    return render(req,'landing.html',{'data1':data})

def order_by(req):
    data = Emp.objects.order_by('Name')
    # data = Emp.objects.order_by('-Name') descending order
    print(data)
    return render(req,'landing.html',{'data2':data})

def Multi_filter(req):
    data = Emp.objects.filter(Name='Krish Gour',Age=18)
    print(data)
    return render(req,'landing.html',{'data3':data})

def exclude(req):
    data=Emp.objects.exclude(City='Delhi')
    print(data)
    return render(req,'landing.html',{'data4':data})