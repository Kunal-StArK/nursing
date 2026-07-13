from django.db import models

# Create your models here.

class Doctors(models.Model):
    doctor_name =models.CharField(max_length=30)
    doctor_specialist= models.CharField(max_length=20)
    doctor_experience = models.TextField()
    doctor_img = models.ImageField(upload_to='uploads', null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)