from django.db import models

# Create your models here.

class BookModel(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    author = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'Book_Image')