from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .forms import SignUpForm,StaffDetailsForm
from .models import StaffUser,StaffDetails
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def StaffDashboard(request):
    staffs = StaffDetails.objects.all()
    #Pass the data
       # Paginate the queryset
    paginator = Paginator(staffs, 10)  # Show 10 students per page
    page_number = request.GET.get('page')
    try:
        staffs = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        staffs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        staffs = paginator.page(paginator.num_pages)
    return render(request,'Staff/StaffDashboard.html', {'staffs': staffs})

def StaffProfile(request, staff_id):
    #  # Retrieve student details from the database
    staff = get_object_or_404(StaffDetails, pk=staff_id)
    #Pass the data
    return render(request,'Staff/StaffProfile.html', {'staff': staff})

def StaffProfileUpdate(request, id):
    staff = StaffDetails.objects.get(id=id)
    
    if request.method == 'POST':
        name =request.POST['name']
        phone = request.POST['phone']
        dob = request.POST['dob']
        age= request.POST['age']
        email =request.POST['email']
        qualification = request.POST['qualification']
        salary =request.POST['salary']
        experience = request.POST['experience']
        designation = request.POST['designation']
        address = request.POST['address']
        # join_date = request.POST['join_data']
        nationality = request.POST['nationality']
        gender = request.POST['gender']
        image = request.POST['image']
        
        
        staff.name= name
        staff.phone = phone
        staff.dob = dob
        staff.age=  age
        staff.email = email
        staff.qualification =  qualification
        staff.salary = salary
        staff.experience =  experience
        staff.designation =  designation
        staff.address =  address
        # staff.join_date = join_data
        staff.nationality = nationality
        staff.gender =  gender
        staff.image =  image
        staff.save()
        messages.success(request,"Updated Successfully")
            # Redirect to the staff profile page after successful update
        return redirect('StaffDashboard')
        
    else:
        messages.error(request, "Failed to update. Please check the form.")
        form = StaffDetailsForm(instance=staff)

    return render(request, 'Staff/StaffProfileUpdate.html', {'form': form, 'staff': staff})

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
def delete(request,id):
    data=StaffDetails.objects.get(id=id)
    data.delete()
    messages.error(request,"Delete Successfully")
    return redirect("StaffDashboard")
