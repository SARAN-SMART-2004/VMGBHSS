from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import StaffUser


def StaffDashboard(request):
    return render(request,'Staff/StaffDashboard.html')
def StaffProfile(request):
    return render(request,'Staff/StaffProfile.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stafflogin')
    else:
        form = SignUpForm()
    return render(request, 'Staff/Signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = StaffUser.objects.filter(username=username, password=password).first()
        if user:
            # Redirect to some page on successful login
            return redirect('StudentDashboard')
        else:
            # Show an error message
            return render(request, 'Staff/login.html', {'error': 'Invalid credentials'})
    return render(request, 'Staff/login.html')
