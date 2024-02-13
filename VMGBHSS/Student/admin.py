from django.contrib import admin

# Register your models here.
from Student.models import StudentUser,StudentDetails
admin.site.register(StudentUser)
admin.site.register(StudentDetails)