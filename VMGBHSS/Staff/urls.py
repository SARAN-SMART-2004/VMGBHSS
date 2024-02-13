from django.urls import path
from . import views



urlpatterns = [
    path('stafflogin',views.login,name='login'),
    path('StaffSignup',views.signup,name='signup'),
    path('StaffDashboard',views.StaffDashboard,name='StaffDashboard'),
    path('StaffProfile',views.StaffProfile,name='StaffProfile'),
]
