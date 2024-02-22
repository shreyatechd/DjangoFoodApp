from django.shortcuts import render
from myfoodapp.models import Contact2
from myfoodapp.models import Res

def web2(request):
     if request.method=="POST":
        name2=request.POST.get('name2')
        email2=request.POST.get('email2')
        phone2=request.POST.get('phone2')
        web2=Contact2(name2=name2, email2=email2, phone2=phone2)
        web2.save()
     return render(request,"web2.html")
def zomato(request):
     if request.method=="POST":
            Restaurant=request.POST.get('Restaurant')
            zomato=Res(Restaurant=Restaurant)
            zomato.save()
     return render(request,"zomato.html")
# Create your views here.
