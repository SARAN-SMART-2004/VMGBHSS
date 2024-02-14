from django.db import models

class StaffUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Define the StudentDetails model
class StaffDetails(models.Model):
    name = models.CharField(max_length=100, null=True )
    phone = models.CharField(max_length=15,null=True )
    dob = models.DateField(blank=True, null=True )
    age= models.IntegerField(blank=True, null=True )
    email = models.EmailField(blank=True,null=True,)
    qualification = models.CharField(max_length=100, null=True  )
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True )
    experience = models.CharField(max_length=100,null=True )
    designation = models.CharField(max_length=100,null=True )
    address = models.TextField(blank=True,null=True,)
    join_date = models.DateField(null=True, blank=True )
    nationality = models.CharField(max_length=100,null=True )
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')] )
    image = models.ImageField(upload_to='staff/images/', null=True )

    # Define string representation of the model
    def __str__(self):
        return self.name