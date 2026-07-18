from django.contrib import admin
from .models import AppointmentModel

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email','date')
    list_filter = ('name','phone')

admin.site.register(AppointmentModel,AppointmentAdmin)    