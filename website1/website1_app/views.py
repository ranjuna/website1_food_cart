from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Pizza,Salad,Noodle


# Create your views here.
def index(request):
    obj=Pizza.objects.all()
    obj2=Salad.objects.all()
    obj3=Noodle.objects.all()
    return render(request,"index.html",{'results':obj,'results2':obj2,'results3':obj3})



