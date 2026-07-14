from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        # Replace these fields with the actual field names present in your Patient model
        fields = ['Patient_name', 'doctor_name','department','gender','admit_time','status'] 

        widgets = {
            'Patient_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Patient Full Name'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Male/Female'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., General, OPD'}),
            'admit_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super(PatientForm, self).__init__(*args, **kwargs)
            self.fields['discharge_time'].required = False