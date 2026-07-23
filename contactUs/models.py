from django.db import models

# Create your models here.

class contact(models.Model):
    full_name= models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    message = models.TextField()
