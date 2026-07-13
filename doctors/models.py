from django.db import models

# Create your models here.

class Doctors(models.Model):
    doctor_name =models.CharField(max_length=30)
    doctor_specialist= models.CharField(max_length=20)
    doctor_experience = models.TextField()
    doctor_img = models.ImageField(upload_to=)