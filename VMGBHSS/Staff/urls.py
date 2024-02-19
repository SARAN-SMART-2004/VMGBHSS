from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from .views import custom_404_view



urlpatterns = [
    path('stafflogin',views.login,name='login'),
    path('StaffSignup',views.signup,name='signup'),
    path('StaffDashboard/',views.StaffDashboard,name='StaffDashboard'),
    path('StaffUpload/', views.StaffUpload, name='StaffUpload'),
    path('StaffProfile/<int:staff_id>/',views.StaffProfile,name='StaffProfile'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('StaffProfileUpdate/<int:id>/',views.StaffProfileUpdate,name='StaffProfileUpdate'),  
]
# Add static file serving for media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = custom_404_view