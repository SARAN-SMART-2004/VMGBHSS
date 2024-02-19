from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
from VMGBHSS.views import error404


urlpatterns = [
    path('',include('Adminuser.urls')),
    path('',include('Staff.urls')),
    path('',include('Student.urls')),
    path('',include('Library.urls')),
    path('admin/', admin.site.urls),
    
    
]
handler404 =error404
