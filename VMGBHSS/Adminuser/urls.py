from django.urls import path
from . import views



urlpatterns = [
    path('contact',views.contact,name='contact'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('AdminPanel',views.AdminPanel,name='AdminPanel'),
    path('Assessment',views.Assessment,name='Assessment'),
    path('Signup',views.signup,name='Signup'),
]

