from django import forms
from .models import StaffUser,StaffDetails

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StaffUser
        fields = ['username', 'email', 'password']
class StaffDetailsForm(forms.ModelForm):
    class Meta:
        model = StaffDetails
        fields = '__all__'  # Include all fields from the model

