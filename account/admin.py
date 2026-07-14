from django.contrib import admin
from .models import Patient
# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display=('name','doctor_name','department','appointment_time','status','created_at')
    list_filter=('name',)

admin.site.register(Patient,PatientAdmin)    