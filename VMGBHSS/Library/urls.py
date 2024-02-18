
# Importing required libraries
from django.urls import path
from . import views


# Url patterns for Books app module of Library Management System
urlpatterns = [
    path('bookhome',views.home,name='bookhome'),
    path('issue',views.issue,name='issue'),
    path('booklogin',views.login,name='booklogin'),
    path('bookregister',views.register,name='bookregister'),
    path('booklogout',views.logout,name='booklogout'),
    path('return_item',views.return_item,name='return_item'),
    path('history',views.history,name='history'),
]