from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'request.html')
def contact(request):
    if request.method =="POST":
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact= Contact(email=email,message=message,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
def signin(request):
    return render(request,'signin.html')