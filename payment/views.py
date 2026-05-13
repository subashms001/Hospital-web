# from django.shortcuts import render
# from django.http import JsonResponse
# from doctors.models import TREATMENT_DETAILS,Appointment

# def get_patient_details(request):
#     patient_id = request.GET.get('patient_id')

#     appointment = Appointment.objects.filter(user_id=patient_id).last()

#     if appointment:
#         treatment = TREATMENT_DETAILS.objects.filter(doctor_name__doctor_name=appointment.doctorname).first()

#         data = {
#             'doctor_name': treatment.doctor_name.id if treatment else '',
#             'treatment_name': treatment.id if treatment else '',
#             'date_of_admit': appointment.date.strftime('%Y-%m-%d'),
#         }
#     else:
#         data = {}

#     return JsonResponse(data)

from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from .forms import DischargeSummaryForm
from .models import DischargeSummary
from doctors.models import ALLDOCTORS, TREATMENT_DETAILS,Appointment


def add_discharge(request):
    if request.method == 'POST':
        form = DischargeSummaryForm(request.POST)
        if form.is_valid():
            discharge =form.save()
            return redirect("final_payment", id=discharge.id)
    else:
        form = DischargeSummaryForm()

    return render(request, 'payment/add_discharge.html', {'form': form})


from django.http import JsonResponse
from doctors.models import Appointment, ALLDOCTORS, TREATMENT_DETAILS

def get_patient_details(request):
    patient_id = request.GET.get('patient_id')

    try:
        appointment = Appointment.objects.filter(user_id=patient_id).latest('date')

        doctor = ALLDOCTORS.objects.get(name=appointment.doctorname)

        treatment = TREATMENT_DETAILS.objects.filter(
            doctor_name=doctor
        ).first()

        return JsonResponse({
            'doctor_id': doctor.id,
            'treatment_id': treatment.id if treatment else '',
            'date_of_admit': appointment.date.strftime('%Y-%m-%d'),
        })

    except Exception as e:
        return JsonResponse({
            'doctor_id': '',
            'treatment_id': '',
            'date_of_admit': '',
            'error': str(e)
        })



def final_payment(request, id):

    discharge = get_object_or_404(DischargeSummary, id=id)

    room_details = {
        "COMMON WARD": {"rate": 900, "medicine_percent": 10},
        "SEMI PRIVATE": {"rate": 2800, "medicine_percent": 12},
        "PRIVATE AC": {"rate": 3750, "medicine_percent": 15},
        "PRIVATE NON AC": {"rate": 3350, "medicine_percent": 13},
        "DELUX": {"rate": 4850, "medicine_percent": 20},
    }

    room_data = room_details.get(discharge.room_type, {"rate": 0, "medicine_percent": 0})

    room_rate = room_data['rate']

    medicine_percent = room_data["medicine_percent"]

    room_charge = room_rate * discharge.total_days

    food_price_per_day = 480

    food_charge =0

    if discharge.food_required:
        food_charge =food_price_per_day* discharge.total_days

    sub_total = room_charge + food_charge

    medicine_charge = sub_total * medicine_percent / 100

    final_amount = sub_total + medicine_charge

    context = {
        "discharge": discharge,
        "room_rate": room_rate,
        "room_charge": room_charge,
        "food_charge": food_charge,
        "medicine_percent": medicine_percent,
        "medicine_charge": medicine_charge,
        "subtotal": sub_total,
        "final_amount": final_amount,
    }

    return render(request,'payment/final_payment.html',context=context)
