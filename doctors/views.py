from django.shortcuts import render, redirect
from doctors.models import ALLDOCTORS
from doctors.models import TREATMENT_DETAILS
from doctors.forms import AppointmentForm

# Create your views here.
def alldoctors(request):
    doctors = ALLDOCTORS.objects.all()
    return render(request, 'doctors/alldoctors.html',{'doctors':doctors})

def treatment(request):
    treat=TREATMENT_DETAILS.objects.all()
    return render(request,'doctors/treatment.html',{'treat':treat})



def doctorslist(request, category):
    # Filters doctors where 'specialisation' matches the treatment's 'category_name'
    doctors = ALLDOCTORS.objects.filter(specialisation=category)
    return render(request, 'doctors/doctorslist.html', {
        'doctors': doctors, 
        'category': category
    })

def appointment(request, doc_name, cat_name):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # We save with commit=False to set the disabled fields manually
            obj = form.save(commit=False)
            obj.user = request.user 
            obj.doctorname = doc_name
            obj.category = cat_name
            obj.consultation_charges = "Rs. 500"
            obj.save()
            return redirect('treatment')
    else:
        # Pre-fill the form fields
        form = AppointmentForm(initial={
            'doctorname': doc_name, 
            'category': cat_name,
            'consultation_charges': "Rs. 500"
        })
    
    return render(request, 'doctors/appointment.html', {'form': form})



