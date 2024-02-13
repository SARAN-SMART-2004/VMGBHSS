from django import forms
from .models import StudentUser,StudentDetails

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StudentUser
        fields = ['username', 'email', 'password']

# Define the form for StudentDetails model
class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = '__all__'  # Include all fields from the model
