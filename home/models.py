from django.db import models

# Create your models here.

class AppointmentModel(models.Model):

    DEPARTMENT_CHOICES = [
        ('General', 'General'),
        ('Cardiology', 'Cardiology'),
        ('Gynaecology & Maternity', 'Gynaecology & Maternity'),
        ('Pediatrics', 'Pediatrics'),
        ('Orthopaedics', 'Orthopaedics'),
        ('General Medicine', 'General Medicine'),
        ('General Surgery', 'General Surgery'),
        ('Other', 'Other'),
    ]

    Gender = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=25)
    gender = models.CharField(max_length=10, choices=Gender)
    date = models.DateField()
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


