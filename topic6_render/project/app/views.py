from django.shortcuts import render

# render = jab apna kisi html page ko show krna chahte ho to render use krte h
# agar html k andar dict data shown krna h to dtl ke tags use hote h {{key}}

# Create your views here.
def my_render(req):
    x=10
    y='python'
    z=[1,2,3,4]
    d = {'p':x,'q':y,'r':z}
    # return render(req,'index.html',{'p':x,'q':y,'r':z})
    return render(req,'index.html',d)  #{'data':d}
