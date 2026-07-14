from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect ('home')


# Dashboard Overview
@login_required(login_url='login')
def dashboard(request):
    # Form submission handle karne ke liye logic
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            if request.user.is_authenticated:
                patient.added_by = request.user.username
            else:
                patient.added_by = "Anonymous"
            patient.save()
            return redirect('dashboard')
    else:
        form = PatientForm()
    patients = Patient.objects.all().order_by('-created_at')
    
    total_patients = patients.count()
    confirmed_appointments = patients.filter(status='Confirmed').count()
    pending_appointments = patients.filter(status='Pending').count()
    
    context = {
        'patients': patients,
        'total_patients': total_patients,
        'confirmed_appointments': confirmed_appointments,
        'pending_appointments': pending_appointments,
        'form': form, 
    }
    return render(request, 'dashboard.html', context)

# 2. Delete Patient View
@login_required(login_url='login')  
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('dashboard')

# 3. Edit Patient View (Direct update karne ke liye simple view)
@login_required(login_url='login')
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == "POST":
        patient.name = request.POST.get('name')
        patient.doctor_name = request.POST.get('doctor_name')
        patient.department = request.POST.get('department')
        patient.admit_time = request.POST.get('admit_time')
        patient.discharge_time = request.POST.get('discharge_time')
        patient.status = request.POST.get('status')
        patient.save()
        return redirect('dashboard')
        
    return render(request, 'edit_patient.html', {'patient': patient})