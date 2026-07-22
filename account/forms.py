from django import forms
from .models import Patient , RegisterModel
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import get_user_model
User = get_user_model()



from doctors.models import Doctors
from about.models import Story, hopitalStats

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Patient_name', 'doctor_name', 'phone', 'email', 'department', 'gender', 'booking_date', 'admit_date', 'status', 'notes'] 

        widgets = {
            'Patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Patient Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Male/Female'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., General, OPD'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'admit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Symptom or comments'}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['admit_date'].required = False
        self.fields['booking_date'].required = False
        self.fields['notes'].required = False

class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['Patient_name', 'doctor_name', 'phone', 'email', 'department', 'gender', 'booking_date', 'admit_date', 'discharge_date', 'status', 'notes'] 

        widgets = {
            'Patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Patient Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Male/Female'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., General, OPD'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'admit_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'discharge_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Symptom or comments'}),
        }

    def __init__(self, *args, **kwargs):
        super(PatientEditForm, self).__init__(*args, **kwargs)
        # Kyunki discharge_date null ho sakti hai, isliye required=False zaroori hai
        self.fields['admit_date'].required = False
        self.fields['booking_date'].required = False
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

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Confirm password'}))

    class Meta:
        model = RegisterModel
        fields = ['first_name', 'last_name', 'phone', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        register_instance = super().save(commit=False)
        
        # Auto-generate username from email (take portion before '@')
        email = register_instance.email
        base_username = email.split('@')[0]
        
        # Create the standard CustomUser record so they can log in
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        # Ensure uniqueness of the generated username
        username = base_username
        counter = 1
        while User.objects.filter(username=username).exists() or RegisterModel.objects.filter(user_name=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
            
        register_instance.user_name = username
        
        if not User.objects.filter(email=register_instance.email).exists():
            user = User.objects.create_user(
                username=username,
                email=register_instance.email,
                first_name=register_instance.first_name,
                last_name=register_instance.last_name,
                phone_number=register_instance.phone,
                password=self.cleaned_data['password']
            )
            user.is_active = True
            user.save()
            
        if commit:
            register_instance.save()
        return register_instance