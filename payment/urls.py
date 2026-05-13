


from django.urls import path
from .views import add_discharge, get_patient_details, final_payment

urlpatterns = [
    path('add-discharge/', add_discharge, name='add-discharge'),
    path('get-patient-details/', get_patient_details, name='get-patient-details'),
    path("final_payment/<int:id>/", final_payment, name="final_payment")
]