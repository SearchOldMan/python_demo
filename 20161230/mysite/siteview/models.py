from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state_province = models.CharField(max_length=40)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    salutation = models.CharField(max_length=60)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='/tmp')

class Book(models.Model):
    title = models.CharField(max_length=40)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication = models.DateField()

