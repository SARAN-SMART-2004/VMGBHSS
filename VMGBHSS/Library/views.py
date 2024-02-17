from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookDetailsForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BookDetails
from Student.models import StudentDetails

# Create your views here.
def BookDashboard(request):
     #  # Retrieve book details from the database
    books = BookDetails.objects.all()
    #Pass the data
      # Paginate the queryset
    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page')
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)
    return render(request,'Library/BookDashboard.html',{'books':books})



def BookProfile(request, book_id):
    #  # Retrieve book details from the database
    book = get_object_or_404(BookDetails, pk=book_id)
    #Pass the data
    return render(request,'Library/BookProfile.html', {'book': book})



def BookProfileUpdate(request,id):
    book=BookDetails.objects.get(id=id)
    if request.POST:
        book_id=request.POST['book_id']
        book_name =request.POST['book_name']
        book_author = request.POST['book_author']
        book_description = request.POST['book_description']
        book_no=request.POST['book_no']
        book_edition=request.POST['book_edition']
        book_publisher=request.POST['book_publisher']
        book_prize=request.POST['book_prize']
        book_language=request.POST['book_language']
        book_isbnno=request.POST['book_isbnno']
        book_publish_year=request.POST['book_publish_year']
        book.book_id= book_id 
        book.book_name= book_name 
        book.book_author = book_author 
        book.book_description = book_description 
        book.book_no=book_no
        book.book_edition=book_edition
        book.book_publisher=book_publisher
        book.book_prize=book_prize
        book.book_language=book_language
        book.book_isbnno=book_isbnno
        book.book_publish_year=book_publish_year

        book.save()
        return redirect('BookDashboard')
    else:
        messages.error(request, "Failed to update. Please check the form.")
        form = BookDetailsForm(instance=book)
    return render(request,'Library/BookProfileUpdate.html',{'form': form,'book':book})

def BookUpload(request):
    if request.method == 'POST':
        form = BookDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BookDashboard')  # Redirect to a success page after successful submission
    else:
        form = BookDetailsForm()
        redirect('home')
    return render(request, 'Library/BookUpload.html', {'form': form})
def delete(request,id):
    book=BookDetails.objects.get(id=id)
    book.delete()
    messages.error(request,"Delete Successfully")
    return redirect("BookDashboard")


        
# Create your views here.
def BookTransaction(request):
     #  # Retrieve book details from the database
    books = BookDetails.objects.all()
    #Pass the data
      # Paginate the queryset
    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page')
    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)
    return render(request,'Library/BookTransaction.html',{'books':books})



def BookIssue(request):
    if request.method == 'POST':
        student_id = request.POST.get('studentId')
        # Assuming you have a Student model with appropriate fields
        student = StudentDetails.objects.get(roll_number=student_id)
        return render(request,'Library/BookIssue.html',{'student':student})
    else:
        # If it's not a POST request, render the form
        return render(request,'Library/BookIssue.html')
