from django.urls import path
from . import views



urlpatterns = [
    path('BookDashboard',views.BookDashboard,name='BookDashboard'),
    path('BookUpload', views.BookUpload, name='BookUpload'),
    path('BookProfile/<int:book_id>/',views.BookProfile,name='BookProfile'),
    path('BookProfileUpdate/<int:id>/',views.BookProfileUpdate,name='BookProfileUpdate'),
    path('BookDelete/<int:id>/',views.delete,name='BookDelete'),
]
