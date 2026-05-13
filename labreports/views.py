from django.shortcuts import render,redirect,get_object_or_404
from labreports.forms import LabtechRegisterationForm, AddLabTestsForm
from labreports.models import Lab_Tests
from django.core.paginator import Paginator

# Create your views here.\
all_lab_tests = [
    {'name': 'Complete Blood Count', 'price': 450, 'time': '6 hours'},
    {'name': 'Liver Function Test', 'price': 700, 'time': '24 hours'},
    {'name': 'Urine Total Test', 'price': 300, 'time': '6 hours'},
    {'name': 'Urine Microscopic Examination', 'price': 350, 'time': '12 hours'},
    {'name': 'Serum Routine Test', 'price': 600, 'time': '24 hours'},
    {'name': 'Thyroid Function Test', 'price': 900, 'time': '48 hours'},
]
def labtechreg(request):
    if request.method == 'POST':
        form = LabtechRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = LabtechRegisterationForm()

    context ={
        'form':form
    }
    return render(request,'labtechs/labtechreg.html',context)



def alltests(request):

    return render(request,'labtechs/alltests.html',{'alltests':all_lab_tests})



def dashboard(request):

    tests = Lab_Tests.objects.all().order_by('created_at')

    paginator = Paginator(tests, 4)
    page_number = request.GET.get('pg')
    page_obj = paginator.get_page(page_number)

    return render(request, 'labtechs/dashboard.html', {'page_obj':page_obj})



def discharge(request):

    return render(request,'labtechs/discharge.html')

def addlab_tests(request,id=None):
    test_obj =None

    if id:
        test_obj = get_object_or_404(Lab_Tests, id=id)

    if request.method == 'POST':
        form = AddLabTestsForm(request.POST,instance=test_obj)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = AddLabTestsForm(instance=test_obj)

    context ={
        'form':form,
        'title': 'Edit Lab Tests' if id else 'Add Lab Tests'
    }
    return render(request,'labtechs/addlabtests.html',context)






