from django.contrib import admin
from .models import Doctors

# Register your models here.

class DoctorsAdmin(admin.ModelAdmin):
    list_display =('doctor_name','doctor_specialist','doctor_experience')


admin.site.register(Doctors,DoctorsAdmin)