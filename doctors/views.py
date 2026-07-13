from django.shortcuts import render
from doctors.models import Doctors

# Create your views here.

def doctorsview(request):
    doctors = Doctors.objects.all()
    return render (request, 'doctors.html',{'doctors':doctors})