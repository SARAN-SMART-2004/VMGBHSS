from django import forms
from .models import BookDetails


# Define the form for StudentDetails model
class BookDetailsForm(forms.ModelForm):
    class Meta:
        model = BookDetails
        fields = '__all__'  # Include all fields from the model
