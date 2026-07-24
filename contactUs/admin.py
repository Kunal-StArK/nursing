from django.contrib import admin
from .models import contact

# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone','email','date','message')

admin.site.register(contact,contactAdmin)