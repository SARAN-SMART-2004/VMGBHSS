from django import forms
from .models import Book,IssuedItem


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author_name', 'quantity', 'subject']
        labels = {
            'book_name': 'Book Name',
            'author_name': 'Author Name',
            'quantity': 'Quantity',
            'subject': 'Subject',
        }
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Book Name'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Author Name'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quantity'}),
            'subject': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Subject', 'rows': 3}),
        }
# Define the form for StudentDetails model
class IssuedItemForm(forms.ModelForm):
    class Meta:
        model = IssuedItem
        fields = '__all__'  # Include all fields from the model
