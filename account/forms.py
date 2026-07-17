from django import forms
from .models import Patient
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from doctors.models import Doctors
from about.models import Story, hopitalStats

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Patient_name', 'doctor_name', 'department', 'gender', 'admit_date', 'status'] 

        widgets = {
            'Patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Patient Full Name'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Male/Female'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., General, OPD'}),
            'admit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Patient_name', 'doctor_name', 'department', 'gender', 'admit_date', 'discharge_date', 'status'] 

        widgets = {
            'Patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Patient Full Name'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Male/Female'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., General, OPD'}),
            'admit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'discharge_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientEditForm, self).__init__(*args, **kwargs)
        # Kyunki discharge_date null ho sakti hai, isliye required=False zaroori hai
        self.fields['discharge_date'].required = False

class AdduserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email',
            'is_active', 
            'is_staff', 
            'is_superuser', 
            'groups', 
            'user_permissions'
        ]

class EdituserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email',
            'is_active', 
            'is_staff', 
            'is_superuser', 
            'groups', 
            'user_permissions'
        ]


class AdddoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = [
            'doctor_name',
            'doctor_specialist',
            'doctor_experience',
            'doctor_img',
            'added_by',
        ]

class EditdoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = [
            'doctor_name',
            'doctor_specialist',
            'doctor_experience',
            'doctor_img',
            'added_by',
        ]

class EditStory(forms.ModelForm):
    class Meta:
        model = Story
        fields = [
            'story_title',
            'story_discription',
        ]


class EditStats(forms.ModelForm):
    class Meta:
        model = hopitalStats
        fields = [
            'year_of_service',
            'expert_doctors',
            'patients_treated',
            'departments',
        ]