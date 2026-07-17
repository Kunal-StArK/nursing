from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import AdduserForm , EdituserForm, PatientRegistrationForm, PatientEditForm, AdddoctorsForm , EditdoctorsForm,EditStory,Addstory,EditStats,Addstats
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from doctors.models import Doctors
from about.models import Story,hopitalStats

# Login / Logout Views
def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('home')

# --- PATIENTS VIEWS ---

@login_required(login_url='login')
def dashboard(request):
    all_patients = Patient.objects.all().order_by('-created_at')
    total_patients = all_patients.count()
    confirmed_appointments = all_patients.filter(status='Confirmed').count()
    pending_appointments = all_patients.filter(status='Pending').count()

    paginator = Paginator(all_patients, 5)  # 5 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'patients': page_obj,  
        'total_patients': total_patients,
        'confirmed_appointments': confirmed_appointments,
        'pending_appointments': pending_appointments,
        'page_obj': page_obj,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def add_patient(request):  
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.added_by = request.user.username
            patient.save()
            return redirect('dashboard')
    else:
        form = PatientRegistrationForm()
    return render(request, 'add_patient.html', {'form': form})

@login_required(login_url='login')
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientEditForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PatientEditForm(instance=patient)
    return render(request, 'edit_patient.html', {'form': form, 'patient': patient})

@login_required(login_url='login')  
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('dashboard')

# --- USERS VIEWS ---

@login_required(login_url='login')
def users(request):
    all_users = User.objects.all()
    paginator = Paginator(all_users, 3)  # 3 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    data = {
        'users': page_obj,  
        'page_obj': page_obj,
    }
    return render(request, 'users.html', data)

@login_required(login_url='login')
def add_user(request):
    if request.method == "POST":
        form = AdduserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = AdduserForm()
    return render(request, 'add_user.html', {'form': form})

@login_required(login_url='login')
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EdituserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EdituserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form})

@login_required(login_url='login')
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')

# Views for doctors
@login_required(login_url='login')
def doctorsall(request):
    all_doctor = Doctors.objects.all()
    data ={
        'all_doctor': all_doctor,
    }
    return render(request,'doctordash.html',data)

@login_required(login_url='login')
def add_doctors(request):
    if request.method == 'POST':
        form = AdddoctorsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('doctorsall')
    else:    
        form = AdddoctorsForm()
    return render(request,'add_doctors.html',{'form': form})

@login_required(login_url='login')
def edit_doctors(request,pk):
    doctor = get_object_or_404(Doctors,pk=pk)
    if request.method == 'POST':
        form = EditdoctorsForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctorsall')
    else:
        form = EditdoctorsForm(instance=doctor)        
    return render(request,'edit_doctors.html',{'form': form})

@login_required(login_url='login')
def delete_doctors(request,pk):
    doctor = get_object_or_404(Doctors,pk=pk)
    doctor.delete()
    return redirect ('doctorsall')


# views for Story
@login_required(login_url='login')
def story(request):
    story = Story.objects.all()
    return render(request,'story.html',{'story':story})

def add_story(request):
    if request.method == 'POST':
        form = Addstory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('story')
    else:
        form = Addstory ()
    return render (request,'add_story.html',{'form': form})

@login_required(login_url='login')
def edit_story(request,pk):
    story = get_object_or_404(Story,pk=pk)
    if request.method == 'POST':
        form = EditStory(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect ('story')
    else:
        form = EditStory (instance=story)
    return render(request,'edit_story.html',{'form': form})



# views for stats
@login_required(login_url='login')
def stats(request):
    stats = hopitalStats.objects.all()
    return render(request,'stats.html',{'stats':stats})

def add_stats(request):
    if request.method == 'POST':
        form = Addstats(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stats')
    else:
        form = Addstats ()
    return render(request,'add_stats.html',{'form':form})
    
@login_required(login_url='login')    
def edit_stats(request,pk):
    stats = get_object_or_404(hopitalStats,pk=pk)
    if request.method == 'POST':
        form = EditStats (request.POST, instance=stats)
        if form.is_valid():
            form.save()
            return redirect('stats')
    else:
        form = EditStats(instance=stats)
    return render (request,'edit_stats.html',{'form':form})