from django.db import models



class Patient(models.Model):

    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ]

    Patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    admit_time = models.TimeField()
    discharge_time = models.TimeField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    added_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name