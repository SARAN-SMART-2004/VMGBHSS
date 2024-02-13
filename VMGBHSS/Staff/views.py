from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm,StaffDetailsForm
from .models import StaffUser,StaffDetails


def StaffDashboard(request):
    staffs = StaffDetails.objects.all()
    #Pass the data
    return render(request,'Staff/StaffDashboard.html', {'staffs': staffs})

def StaffProfile(request, staff_id):
    #  # Retrieve student details from the database
    staff = get_object_or_404(StaffDetails, pk=staff_id)
    #Pass the data
    return render(request,'Staff/StaffProfile.html', {'staff': staff})

def StaffUpload(request):
    if request.method == 'POST':
        form = StaffDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page after successful submission
    else:
        form = StaffDetailsForm()
    return render(request, 'Staff/StaffUpload.html', {'form': form})

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
