from django.db import models

class StaffUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Define the StudentDetails model
class StaffDetails(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    join_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    image = models.ImageField(upload_to='staff/images/', null=True, blank=True)

    # Define string representation of the model
    def __str__(self):
        return self.name