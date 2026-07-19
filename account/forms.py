from django import forms
from .models import Patient
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import get_user_model

User = get_user_model()

from doctors.models import Doctors
from about.models import Story, hopitalStats

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Patient_name', 'doctor_name', 'phone', 'email', 'department', 'gender', 'admit_date', 'status', 'notes'] 

        widgets = {
            'Patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Patient Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Male/Female'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., General, OPD'}),
            'admit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Symptom or comments'}),
        }

class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Patient_name', 'doctor_name', 'phone', 'email', 'department', 'gender', 'admit_date', 'discharge_date', 'status', 'notes'] 

        widgets = {
            'Patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Patient Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Male/Female'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., General, OPD'}),
            'admit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'discharge_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Symptom or comments'}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientEditForm, self).__init__(*args, **kwargs)
        # Kyunki discharge_date null ho sakti hai, isliye required=False zaroori hai
        self.fields['discharge_date'].required = False
        self.fields['notes'].required = False


class AdduserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'username', 
            'email',
            'phone_number',
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
            'phone_number',
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


class Addstory(forms.ModelForm):
    class Meta:
        model = Story
        fields = [
            'story_title',
            'story_discription',
        ]


class EditStory(forms.ModelForm):
    class Meta:
        model = Story
        fields = [
            'story_title',
            'story_discription',
        ]


class Addstats(forms.ModelForm):
    class Meta:
        model = hopitalStats
        fields = [
            'year_of_service',
            'expert_doctors',
            'patients_treated',
            'departments',
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