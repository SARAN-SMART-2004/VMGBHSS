from django.contrib import admin
from .models import Book ,IssuedItem

# Register your models here.
class BookFilter(admin.ModelAdmin):
    list_display = ("book_name","author_name","quantity","subject")
    list_filter = ("book_name","author_name","subject","book_add_date")
    search_fields = ("book_name","author_name","subject")
    
admin.site.register(Book,BookFilter)

class IssuedItemFilter(admin.ModelAdmin):
    list_display = ("book_name","username","issue_date","return_date")
    list_filter = ("issue_date","return_date","book_id__book_name","user_id__username") 
    search_fields = ("user_id__username","book_id__book_name","book_id__subject")

admin.site.register(IssuedItem,IssuedItemFilter)