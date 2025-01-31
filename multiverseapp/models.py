from django.db import models

# Create your models here.

from django.db import models

class Designs(models.Model):
    TAG_CHOICES = [
        ('abstract', 'Abstract'),
        ('metal', 'Metal'),
        ('pop', 'Pop'),
        ('anime', 'Anime'),
        ('minimals', 'Minimals'),
        ('cartoon', 'Cartoon'),
        ('fiction', 'Fiction'),
    ]

    image = models.CharField(max_length=1000)
    title = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255, unique=True)
    price = models.CharField(max_length=250)
    tag = models.CharField(max_length=25, choices=TAG_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Products(models.Model):
    CAT_CHOICES = [
        ('trending', 'Trending'),
        ('thrifted', 'Thrifted'),         
    ]

    image = models.CharField(max_length=1000)
    heading = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255, unique=True)
    price = models.CharField(max_length=250)
    cat= models.CharField(max_length=25, choices=CAT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading