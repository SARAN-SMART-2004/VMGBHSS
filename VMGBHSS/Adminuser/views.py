from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import User

# Create your views here.
def base(request):
    return render(request,'Adminuser/base.html')
def contact(request):
    return render(request,'Adminuser/contact.html')

def home(request):
    
    return render(request,'Adminuser/home.html')

def AdminPanel(request):
    return render(request,'Adminuser/adminpanel.html')
def Assessment(request):
    return render(request,'Adminuser/Assessment.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'Adminuser/Signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            # Redirect to some page on successful login
            return redirect('home')
        else:
            # Show an error message
            return render(request, 'Adminuser/login.html', {'error': 'Invalid credentials'})
    return render(request, 'Adminuser/login.html')
