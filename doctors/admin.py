from django.contrib import admin
from doctors.models import ALLDOCTORS
from doctors.models import TREATMENT_DETAILS
from doctors.models import Appointment
admin.site.register(ALLDOCTORS)
admin.site.register(TREATMENT_DETAILS)
admin.site.register(Appointment)



# Register your models here.
