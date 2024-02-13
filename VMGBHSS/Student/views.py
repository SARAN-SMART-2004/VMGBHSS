
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import StudentUser,StudentDetails

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlogin')
    else:
        form = SignUpForm()
    return render(request, 'Student/Signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = StudentUser.objects.filter(username=username, password=password).first()
        if user:
            # Redirect to some page on successful login
            return redirect('home')
        else:
            # Show an error message
            return render(request, 'Student/login.html', {'error': 'Invalid credentials'})
    return render(request, 'Student/login.html')

def StudentDashboard(request):
     #  # Retrieve student details from the database
    students = StudentDetails.objects.all()
    #Pass the data
    
    return render(request,'Student/StudentDashboard.html', {'students': students})
def StudentProfile(request, student_id):
    #  # Retrieve student details from the database
    student = get_object_or_404(StudentDetails, pk=student_id)
    #Pass the data
    return render(request,'Student/StudentProfile.html', {'student': student})
