from django.db import models

# Create your models here.

# Define the BookDetails model
class BookDetails(models.Model):
    # Define fields
    book_id=models.IntegerField()
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=15)
    book_description = models.TextField()
    
    # Define string representation of the model
    def __str__(self):
        return self.name

    