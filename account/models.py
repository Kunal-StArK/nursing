from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
