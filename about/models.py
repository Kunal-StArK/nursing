from django.db import models

# Create your models here.
class Story(models.Model):
    story_title = models.CharField(max_length=100)
    story_description = models.TextField()
    img= models.ImageField(upload_to='uploads', null=True,blank=True)


class hopitalStats (models.Model):
    year_of_service = models.IntegerField()
    expert_doctors = models.IntegerField()
    patients_treated = models.IntegerField()
    departments = models.IntegerField()
