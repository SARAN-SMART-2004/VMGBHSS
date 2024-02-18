from django import forms
from .models import Book,IssuedItem


# Define the form for StudentDetails model
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields from the model

# Define the form for StudentDetails model
class IssuedItemForm(forms.ModelForm):
    class Meta:
        model = IssuedItem
        fields = '__all__'  # Include all fields from the model
