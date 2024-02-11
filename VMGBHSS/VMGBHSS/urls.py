from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',include('Adminuser.urls')),
    path('',include('Staff.urls')),
    path('',include('Student.urls')),
    path('admin/', admin.site.urls),
    
]
