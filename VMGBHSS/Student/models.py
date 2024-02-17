from django.db import models

class StudentUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Define the StudentDetails model
class StudentDetails(models.Model):
    # Define fields
    name = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    father_name = models.CharField(max_length=100)
    caste = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    mother_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    first_language = models.CharField(max_length=50)
    medium_of_language = models.CharField(max_length=50)
    emis_no = models.CharField(max_length=20)
    admission_no = models.CharField(max_length=20)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=gender_choices)
    roll_number=models.IntegerField(null=True)
    category=models.CharField(max_length=20,null=True)
    
    
    # Define string representation of the model
    def __str__(self):
        return self.name

    