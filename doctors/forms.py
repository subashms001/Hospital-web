from doctors.models import Appointment
from django import forms

class AppointmentForm (forms.ModelForm):
    doctorname=forms.CharField(required=False)
    category=forms.CharField(required=False)
    consultation_charges=forms.CharField(required=False)  #non editable field
    class Meta:
        model=Appointment
        fields=['doctorname', 'category', 'date', 'time', 'consultation_charges']
        widgets = {
            'time': forms.Select(attrs={'class': 'form-control'}), # Creates the dropdown
        }