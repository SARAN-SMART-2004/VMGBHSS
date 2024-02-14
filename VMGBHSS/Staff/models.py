from django.db import models

class StaffUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Define the StudentDetails model
class StaffDetails(models.Model):
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    dob = models.DateField(blank=True)
    age= models.IntegerField(blank=True)
    email = models.EmailField(blank=True,null=True,)
    qualification = models.CharField(max_length=100, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    experience = models.CharField(max_length=100,null=True, blank=True)
    designation = models.CharField(max_length=100,null=True, blank=True)
    address = models.TextField(blank=True,null=True,)
    join_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100,null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)
    image = models.ImageField(upload_to='staff/images/', null=True, blank=True)

    # Define string representation of the model
    def __str__(self):
        return self.name