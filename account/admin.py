from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display=('Patient_name','doctor_name')

admin.site.register(Patient,PatientAdmin)    