from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from doctors.models import Doctors
from .models import Patient

# Create your views here.

def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect ('dashboard')

    form = AuthenticationForm()
    data = {
        'form': form,
    }
    return render(request,'login.html',data)


def logout(request):
    auth.logout(request)
    return redirect ('home')


# Dashboard Overview
def dashboard(request):
    patients = Patient.objects.all().order_by('-created_at')
    
    # Cards ke stats ko calculate karne ke liye dynamic logic
    total_patients = patients.count()
    confirmed_appointments = patients.filter(status='Confirmed').count()
    pending_appointments = patients.filter(status='Pending').count()
    
    context = {
        'patients': patients,
        'total_patients': total_patients,
        'confirmed_appointments': confirmed_appointments,
        'pending_appointments': pending_appointments,
    }
    return render(request, 'dashboard.html', context)

# 2. Delete Patient View
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('dashboard')

# 3. Edit Patient View (Direct update karne ke liye simple view)
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == "POST":
        patient.name = request.POST.get('name')
        patient.doctor_name = request.POST.get('doctor_name')
        patient.department = request.POST.get('department')
        patient.appointment_time = request.POST.get('appointment_time')
        patient.discharge_time = request.POST.get('discharge_time')
        patient.status = request.POST.get('status')
        patient.save()
        return redirect('dashboard')
        
    return render(request, 'edit_patient.html', {'patient': patient})