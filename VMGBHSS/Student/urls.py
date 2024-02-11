from django.urls import path
from . import views



urlpatterns = [
   
    path('studentlogin',views.login,name='login'),
    path('StudentDashboard',views.StudentDashboard,name='StudentDashboard'),
    path('StudentProfile',views.StudentProfile,name='StudentProfile'),
]
