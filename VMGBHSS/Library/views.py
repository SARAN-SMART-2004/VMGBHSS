
# Importing required libraries
from django.shortcuts import redirect, render
from .models import Book, IssuedItem
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import date
from django.core.paginator import Paginator


# ----------------- Library Management System Views -----------------

# Home view
def home(request):
    return render(request,'Library/home.html')

# Login view to login user
def login(request):

    # If request is post then get username and password from request
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = auth.authenticate(username=username,password=password)

        # If user is authenticated then login user
        if(user is not None):
            auth.login(request,user)

            # Redirect to home page
            return redirect('/bookhome')
        else:

            # If user is not authenticated then show error message
            # and redirect to login page
            messages.info(request,'Invalid Credential')
            return redirect('booklogin')
    else:

        # If request is not post then render login page
        return render(request,'Library/login.html')


# Register view to register user
def register(request):

    # If request is post then get user details from request
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if password and confirm password matches
        if(password1 == password2):

            # Check if username or email already exists
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username already exist')
                return redirect('bookregister')
            
            # Check if email already exists
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'Email already registered')
                return redirect('bookregister')
            
            # If username and email does not exists then create user
            else:

                # Create user
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                
                # Save user
                user.save()

                # Redirect to login page
                return redirect('booklogin')
        else:

            # If password and confirm password does not matches then show error message
            messages.info(request,'Password not matches')
            return redirect('bookregister')
    else:

        # If request is not post then render register page
        return render(request,'Library/register.html')


# Logout view to logout user
def logout(request):

    # Logout user and redirect to home page
    auth.logout(request)
    return redirect('bookhome')


# Issue view to issue book to user
@login_required(login_url='login')
def issue(request):

    # If request is post then get book id from request
    if(request.method == 'POST'):
        book_id = request.POST['book_id']
        current_book = Book.objects.get(id=book_id)
        book = Book.objects.filter(id=book_id)
        issue_item = IssuedItem.objects.create(user_id=request.user,book_id=current_book)
        issue_item.save()
        book.update(quantity = book[0].quantity-1)

        # Show success message and redirect to issue page
        messages.success(request, 'Book issued successfully.')

    # Get all books which are not issued to user
    my_items = IssuedItem.objects.filter(user_id = request.user,return_date__isnull=True).values_list('book_id')
    books = Book.objects.exclude(id__in=my_items).filter(quantity__gt=0)

    # Return issue page with books that are not issued to user
    return render(request,'Library/issue_item.html',{'books':books})

# History view to show history of issued books to user
@login_required(login_url='booklogin')
def history(request):

    # Get all issued books to user
    my_items = IssuedItem.objects.filter(user_id=request.user).order_by('-issue_date')

    # Paginate data
    paginator = Paginator(my_items,10) 

    # Get page number from request
    page_number = request.GET.get('page')
    show_data_final = paginator.get_page(page_number)

    # Return history page with issued books to user
    return render(request,'Library/history.html',{'books':show_data_final})


# Return view to return book to library
@login_required(login_url='booklogin')
def return_item(request):

    # If request is post then get book id from request
    if(request.method == 'POST'):

        # Get book id from request
        book_id = request.POST['book_id']

        # Get book object
        current_book = Book.objects.get(id=book_id)

        # Update book quantity
        book = Book.objects.filter(id=book_id)
        book.update(quantity = book[0].quantity+1)

        # Update return date of book and show success message
        issue_item = IssuedItem.objects.filter(user_id=request.user,book_id=current_book,return_date__isnull=True)
        issue_item.update(return_date=date.today())
        messages.success(request, 'Book returned successfully.')

    # Get all books which are issued to user
    my_items = IssuedItem.objects.filter(user_id = request.user,return_date__isnull=True).values_list('book_id')
    
    # Get all books which are not issued to user
    books = Book.objects.exclude(~Q(id__in=my_items))

    # Return return page with books that are issued to user
    params = {'books':books}
    return render(request,'Library/return_item.html',params)
