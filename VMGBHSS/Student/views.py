
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm,StudentDetailsForm
from django.contrib import messages
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



def StudentProfileUpdate(request,id):
    student=StudentDetails.objects.get(id=id)
    if request.POST:
        name=request.POST['name']
        dob=request.POST['dob']
        phone =request.POST['phone']
        class_name =request.POST['class_name']
        section =request.POST['section']
        blood_group=request.POST['blood_group']
        father_name =request.POST['father_name']
        caste =request.POST['caste']
        email =request.POST['email']
        address=request.POST['address']
        mother_name =request.POST['mother_name']
        nationality =request.POST['nationality']
        first_language=request.POST['first_language']
        medium_of_language =request.POST['medium_of_language']
        emis_no =request.POST['emis_no']
        admission_no =request.POST['admission_no']
        gender =request.POST['gender']

        student.name= name 
        student.dob= dob 
        student.phone = phone 
        student.class_name = class_name 
        student.section = section 
        student.blood_group= blood_group 
        student.father_name = father_name 
        student.caste = caste 
        student.email = email 
        student.address= address 
        student.mother_name = mother_name 
        student.nationality = nationality 
        student.first_language= first_language 
        student.medium_of_language = medium_of_language 
        student.emis_no = emis_no 
        student.admission_no = admission_no 
        student.gender = gender 
        student.save()
        return redirect('StudentDashboard')
    else:
        messages.error(request, "Failed to update. Please check the form.")
        form = StudentDetailsForm(instance=student)
    return render(request,'Student/StudentProfileUpdate.html',{'form': form,'student':student})

def StudentUpload(request):
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('StudentDashboard')  # Redirect to a success page after successful submission
    else:
        form = StudentDetailsForm()
        redirect('home')
    return render(request, 'Student/StudentUpload.html', {'form': form})

        
