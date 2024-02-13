from django import forms
from .models import StaffUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StaffUser
        fields = ['username', 'email', 'password']
