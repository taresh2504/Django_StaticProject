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
    data = Emp.objects.filter(Name='Krish',Age=18)
    print(data)
    return render(req,'landing.html',{'data3':data})

def exclude(req):
    data=Emp.objects.exclude(City='Delhi')
    print(data)
    return render(req,'landing.html',{'data4':data})

def get(req):
    data = Emp.objects.get(Age=19)
    print(data)
    return render(req,'landing.html',{'data5':data})

def first(req):
    data=Emp.objects.first()
    print(data)
    return render(req,'landing.html',{'data6':data})

def last(req):
    data=Emp.objects.last()
    print(data)
    return render(req,'landing.html',{'data7':data})
    
def earliest(req):
    data=Emp.objects.earliest('City')
    print(data)
    return render(req,'landing.html',{'data8':data})

def latest(req):
    data=Emp.objects.latest('Name')
    print(data)
    return render(req,'landing.html',{'data9':data})

def create(req):
    data=Emp.objects.create(Name='Neeraj',Email='neeraj@gmail.com',Age=50,City='Rewa')
    all_data=Emp.objects.all()
    return render(req,'landing.html',{'data':all_data})

def b_create(req):
    data=Emp.objects.bulk_create([Emp(Name='Neeraj2',Email='neeraj2@gmail.com',Age=50,City='Rewa'),Emp(Name='Neeraj3',Email='neeraj3@gmail.com',Age=50,City='Rewa'),Emp(Name='Neeraj4',Email='neeraj4@gmail.com',Age=50,City='Rewa')])
    all_data=Emp.objects.all()
    return render(req,'landing.html',{'data':all_data})

def delete(req):
    num = int(req.POST.get('number'))
    data = Emp.objects.get(id=num)
    data.delete()
    all_data=Emp.objects.all()
    return render(req,'landing.html',{'data':all_data})

def m_delete(req):
    num = req.POST.get('number1')
    print(num)
    num = num.split(',')
    print(num)
    for i in num:
        data=Emp.objects.get(id=int(i))
        data.delete()
    all_data=Emp.objects.all()
    return render(req,'landing.html',{'data':all_data})    



    
    