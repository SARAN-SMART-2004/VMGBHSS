from django.db import models


# Create your models here.

# Define the BookDetails model
class BookDetails(models.Model):
    # Define fields
    book_id=models.IntegerField()
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=55)
    book_description = models.TextField()
    book_no=models.IntegerField(null=True)
    book_edition=models.CharField(null=True,max_length=95)
    book_publisher=models.CharField(null=True,max_length=95)
    book_prize=models.IntegerField(null=True)
    book_language=models.CharField(null=True,max_length=15)
    book_isbnno=models.IntegerField(null=True)
    book_publish_year=models.CharField(null=True,max_length=15)
    
    # Define string representation of the model
    def __str__(self):
        return self.name


