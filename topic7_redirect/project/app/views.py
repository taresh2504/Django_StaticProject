from django.shortcuts import render
from django.shortcuts import redirect

# redirect = ek url se dusra url ko call krne k liye hota h.2 type k hote h 
# external :- matlab ki external site pe bhejna. ex = facebook,google,instagram
# internal :- matlab ki kisi internal page par bhejna

# Create your views here.
def external_redirect(req):
    return redirect("https://www.facebook.com/")

def internal_redirect(req):
    return redirect("first",x=10)

def internal_redirect2(req):
    return render(req,'index.html')
