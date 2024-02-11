from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'Student/login.html')
def StudentDashboard(request):
    return render(request,'Student/StudentDashboard.html')
def StudentProfile(request):
    return render(request,'Student/StudentProfile.html')
