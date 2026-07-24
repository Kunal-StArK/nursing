from django.shortcuts import render,redirect
from about.models import hopitalStats
from account.models import Patient
from django.contrib import messages

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

def galleryview(request):
    return render (request, 'gallery.html')

def book_appointment(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        date = request.POST.get('date')
        department = request.POST.get('department')
        notes = request.POST.get('notes')

        Patient.objects.create(
            Patient_name=name,
            phone=phone,
            email=email,
            gender=gender if gender else 'Other',
            booking_date=date,
            department=department,
            notes=notes,
            status='Pending',
            added_by='Online Booking',
            doctor_name='Not Assigned'
        )

        messages.success(request, 'Your appointment request has been sent! We will call you soon.')
        return redirect('book_appointment')
    return render(request, 'book_appointment.html')


