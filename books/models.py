from django.db import models

class Details(models.Model):
    Book = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Language  = models.CharField(max_length=100)
    Published_on = models.IntegerField()
    Sales_in_millions = models.IntegerField()
    Genre = models.CharField(max_length=50)

    def __str__(self):
        return self.Book
