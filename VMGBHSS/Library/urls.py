
# Importing required libraries
from django.urls import path
from . import views
from django.conf.urls import handler404
from .views import custom_404_view

# Url patterns for Books app module of Library Management System
urlpatterns = [
    path('bookhome',views.home,name='bookhome'),
    path('issue',views.issue,name='issue'),
    path('booklogin',views.login,name='booklogin'),
    path('bookregister',views.register,name='bookregister'),
    path('booklogout',views.logout,name='booklogout'),
    path('return_item',views.return_item,name='return_item'),
    path('history',views.history,name='history'), 
    path('addbook', views.add_book, name='add_book'),
]
handler404 = custom_404_view