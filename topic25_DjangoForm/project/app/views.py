from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def register(req):
    if req.method == 'POST':
        form = StudentForm(req.POST)
        if form. is_valid():
            form.save()
            return redirect('landing')
        # print(xyz)
        # print(xyz.cleaned_data)
    else:    
        form = StudentForm()
        return render(req,'register.html',{'form':form})
