from django.shortcuts import render,redirect
from about.models import hopitalStats

# Create your views here.

def homeview(request):
    hospitalstats= hopitalStats.objects.order_by('-id').first()
    data={
        'hospitalstats': hospitalstats,
    }
    return render (request, 'home.html', data)

def servicesview(request):
    return render (request, 'services.html')

def departmentsview(request):
    return render (request, 'departments.html')

def contactview(request):
    return render (request, 'contact.html')

def galleryview(request):
    return render (request, 'gallery.html')
