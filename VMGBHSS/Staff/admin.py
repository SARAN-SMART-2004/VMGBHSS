from django.contrib import admin

# Register your models here.
from Staff.models import StaffUser,StaffDetails
admin.site.register(StaffUser)
admin.site.register(StaffDetails)