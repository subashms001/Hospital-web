from django import forms
from .models import DischargeSummary
from django.contrib.auth.models import User
from doctors.models import TREATMENT_DETAILS, Appointment


class DischargeSummaryForm(forms.ModelForm):
    class Meta:
        model = DischargeSummary
        exclude = ['total_days', 'date_of_discharge']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        patient_ids = Appointment.objects.values_list('user_id', flat=True).distinct()
        self.fields['patient_name'].queryset = User.objects.filter(id__in=patient_ids)
