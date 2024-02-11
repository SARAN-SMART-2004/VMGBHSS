from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'Staff/login.html')
def StaffDashboard(request):
    return render(request,'Staff/StaffDashboard.html')
def StaffProfile(request):
    return render(request,'Staff/StaffProfile.html')
