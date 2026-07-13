from django.db import models

# Create your models here.
class Story(models.Model):
    story_title = models.CharField(max_length=100)
    story_discription = models.TextField()


class hopitalStats (models.Model):
    year_of_service = models.IntegerField()
    expert_doctors = models.IntegerField()
    patients_treated = models.IntegerField()
    departments = models.IntegerField()
