from django.urls import path
from . import views
from django.conf.urls import handler404
from .views import custom_404_view



urlpatterns = [
    path('contact',views.contact,name='contact'),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('AdminPanel/',views.AdminPanel,name='AdminPanel'),
    path('Assessment/',views.Assessment,name='Assessment'),
    path('Signup/',views.signup,name='Signup'),
]

handler404 = custom_404_view