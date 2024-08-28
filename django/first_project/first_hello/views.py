from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime



 



def home(request):
    return HttpResponse(f"hello world!")





def gabi(request):
    return HttpResponse("<body style=\"background:blue\"> <h1 style=\"color:#FFC0CB\">hello gabi</h1></body>")   




#def greet(request,name):
    return render(request, "first_hello/index.html",{
        "name":name.upper()
    })
    

def newyear(request):
    now=datetime.now()
    return render(request, "first_hello/novano.html",{
        "new_year": now.day==1 and now.month==1
    })