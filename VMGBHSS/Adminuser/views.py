from django.shortcuts import render
# Create your views here.
def base(request):
    return render(request,'Adminuser/base.html')
def contact(request):
    return render(request,'Adminuser/contact.html')

def home(request):
    return render(request,'Adminuser/home.html')
def login(request):
    return render(request,'Adminuser/login.html')
def AdminPanel(request):
    return render(request,'Adminuser/adminpanel.html')
def Assessment(request):
    return render(request,'Adminuser/Assessment.html')