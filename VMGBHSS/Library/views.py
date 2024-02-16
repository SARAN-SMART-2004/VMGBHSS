from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookDetailsForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import BookDetails

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

        book.book_id= book_id 
        book.book_name= book_name 
        book.book_author = book_author 
        book.book_description = book_description 

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


        
