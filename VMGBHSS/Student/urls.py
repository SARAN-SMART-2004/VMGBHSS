from django.urls import path
from . import views



urlpatterns = [
    path('StudentSignup',views.signup,name='signup'),
    path('studentlogin',views.login,name='login'),
    path('StudentDashboard',views.StudentDashboard,name='StudentDashboard'),
    path('StudentUpload', views.StudentUpload, name='StudentUpload'),
    path('StudentProfile/<int:student_id>/',views.StudentProfile,name='StudentProfile'),
    path('StudentProfileUpdate/<int:id>/',views.StudentProfileUpdate,name='StudentProfileUpdate'),
]
